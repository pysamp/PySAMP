@ECHO OFF

SET WORKSPACE_DIR=%CD:\=/%

git clone https://github.com/habecker/PySAMP.git
git clone https://github.com/habecker/sampgdk.git
git clone https://github.com/Zeex/samp-plugin-sdk.git

pip install ply
IF EXIST sampgdk/build (
   rmdir /s/q sampgdk/build
)
cd sampgdk
mkdir build
mkdir local
cd build
cmake .. -DSAMP_SDK_ROOT=%WORKSPACE_DIR%/samp-plugin-sdk -DSAMPGDK_STATIC=ON -DSAMPGDK_BUILD_AMALGAMATION=ON -DCMAKE_INSTALL_PREFIX=%WORKSPACE_DIR%/sampgdk/local
cmake --build %WORKSPACE_DIR%/sampgdk/build --config Release
cmake --build %WORKSPACE_DIR%/sampgdk/build --config Release --target install
cd ../..
cd PySAMP
mkdir build
cd build
cmake -DSAMPSDK_DIR=%WORKSPACE_DIR%/samp-plugin-sdk -DSAMPGDK_DIR=%WORKSPACE_DIR%/sampgdk -DCMAKE_PREFIX_PATH="%WORKSPACE_DIR%\sampgdk\local" ../src
cd ../..

%WORKSPACE_DIR%/PySAMP/build/PySAMP.vcxproj