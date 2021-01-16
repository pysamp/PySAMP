from samp import *
import os

def LoadStaticVehiclesFromFile(filename):
    vehicles_loaded = 0
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                index = 0

                index = line.split(",")
                if len(index) < 1:
                    continue
                
                vehicletype = int(index[0])
                SpawnX = float(index[1])
                SpawnY = float(index[2]) 
                SpawnZ = float(index[3])
                SpawnRot = float(index[4])
                Color1 = int(index[5])
                Color2 = int(index[6].split(";")[0]) 
                #There are comments at the end of the line so i am cutting that off

                
                if vehicletype < 400 or vehicletype > 611: 
                    continue
                if (
                index[0] == -1 or
                index[1] == -1 or
                index[2] == -1 or
                index[3] == -1 or
                index[4] == -1
                ):
                    continue

                AddStaticVehicleEx(vehicletype,SpawnX,SpawnY,SpawnZ,SpawnRot,Color1,Color2,(30*60)) # respawn 30 minutes
                vehicles_loaded +=1
            f.close()
            print("Loaded {} vehicles from: {}".format(int(vehicles_loaded),filename))
    except IOError as error:
        print(error)


    return int(vehicles_loaded)