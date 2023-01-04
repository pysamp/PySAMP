from pysamp import add_static_vehicle_ex
import os

def load_from_file(filename):
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
                spawn_x = float(index[1])
                spawn_y = float(index[2]) 
                spawn_z = float(index[3])
                spawn_rot = float(index[4])
                color_1 = int(index[5])
                color_2 = int(index[6].split(";")[0]) 
  
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

                add_static_vehicle_ex(vehicletype, spawn_x, spawn_y, spawn_z, spawn_rot, color_1, color_2, 1800)
                vehicles_loaded +=1
            f.close()
            print("Loaded {} vehicles from: {}".format(int(vehicles_loaded),filename))
    except IOError as error:
        print(error)
