import numpy as np
#pcd head
HEADER = '''\
# .PCD v0.7 - Point Cloud Data file format
VERSION 0.7
FIELDS x y z intensity
SIZE 4 4 4 4 
TYPE F F F F 
COUNT 1 1 1 1 
WIDTH {}
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS {}
DATA ascii
'''

path=r'G:\博士后材料\专利\机器人\图\20200901\1599013438.05\pcds\000000.npy'
pathbin=r'G:\博士后材料\专利\机器人\图\20200901\1599013438.05\images\000003.bin'



#for kitti
def kitti_velodyne_reader(velo_filename):
    scan = np.fromfile(velo_filename, dtype=np.float32)
    scan = scan.reshape((-1, 4))
    max=np.max(scan[:,3])
    min=np.min(scan[:,3])
    mum=max-min
    for i in range(0,scan.shape[0]):
        scan[i,3]=int((scan[i,3]-min)/mum*255)
    return scan

#for npy
pc = np.load(path)

#read pcd
def load_pcd_to_ndarray(pcd_path):
    with open(pcd_path) as f:
        while True:
            ln = f.readline().strip()
            if ln.startswith('DATA'):
                break

        points = np.loadtxt(f)
        points = points[:, 0:4]
        return points

#write pcd
def write_pcd(points, save_pcd_path):
    with open(save_pcd_path, 'w') as f:
        f.write(HEADER.format(len(points), len(points)) + '\n')
        np.savetxt(f, points, delimiter = ' ', fmt = '%f %f %f %d')

bin=load_velo_scan(pathbin)

write_pcd(pc,'./1.pcd')
write_pcd(bin,'./2.pcd')