
$script_path = split-path -parent $MyInvocation.MyCommand.Definition
$script_path = [System.String]::Concat($script_path, "\server")
Set-Location $script_path

$pysamp_path='..\build\PySAMP.so'
$pysamp_module_path='..\..\pysamp'

if ( !(Test-Path $pysamp_path) )
{  
    Set-Location "../build"
    ./build_pysamp.ps1
    Set-Location $script_path
    Copy-Item $pysamp_path ./
    Copy-Item -Path $pysamp_module_path -Destination ./ -Force -Recurse
    docker build --no-cache --platform linux/amd64 -t pysamp/server .

    Remove-Item -Path (Get-Item $pysamp_path).Name
    Remove-Item -Path ./pysamp -Force -Recurse
}

docker run --name pysamp_server --platform linux/amd64 -v "$PWD/../data:/server" -p 7777:7777/udp --rm -ti pysamp/server