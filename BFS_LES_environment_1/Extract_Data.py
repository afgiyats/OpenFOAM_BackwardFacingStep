
from paraview.simple import *

paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
foamfoam = OpenFOAMReader(registrationName='bfs_simple.foam', FileName='.\\bfs_LES_environment_simple\\foam.foam')
foamfoam.MeshRegions = ['internalMesh']
foamfoam.CellArrays = ['U', 'UMean', 'UPrime2Mean', 'k', 'nut', 'p', 'pMean', 'pPrime2Mean', 's']
 
# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on foamfoam
foamfoam.SkipZeroTime = 0

UpdatePipeline(time=0.01, proxy=foamfoam)

# Properties modified on foamfoam
foamfoam.CellArrays = ['U', 'p']

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=foamfoam)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.02500000037252903, 0.007499999832361937, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.02500000037252903, 0.007499999832361937, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# save data
SaveData('${pwd}/CSV_FILEs/OpenFOAM.csv', proxy=slice1, WriteTimeSteps=1,
    PointDataArrays=['U', 'p'],
    CellDataArrays=['U', 'p'],
    FieldDataArrays=['CasePath'],
    AddTime=1)