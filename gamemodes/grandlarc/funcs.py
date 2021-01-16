from samp import *
import os

def LoadStaticVehiclesFromFile(filename):
    vehicles_loaded = 0
    print("Loc: {}".format(os.getcwd()))
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                index = 0

                index = line.split(",")
                if len(index) < 1:
                    continue
                
                vehicletype = index[0]
                SpawnX = float(index[1])
                SpawnY = float(index[2]) 
                SpawnZ = float(index[3])
                SpawnRot = float(index[4])
                Color1 = index[5]
                Color2 = index[6]

                
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
            print("Loaded {} vehicles from: {}".format(vehicles_loaded,filename))
    except IOError as error:
        print(error)


    return vehicles_loaded