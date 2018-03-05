from numpy import *

def loadDataSet(filename):
    dataMat=[]
    fr=open(filename)
    for line in fr.readlines():
        curLine=line.strip().split('\t')
        fltLine=map(float,curLine)
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA,vecB):
    return sqrt(sum(power(vecA-vecB,2)))

def randCent(dataSet,k):
    n=shape(dataSet)[1]
    centroids=mat(zeros((k,n)))
    for j in range(n):
        minJ=min(dataSet[:,j])
        rangeJ=float(max(array(dataSet)[:,j])-minJ)
        centroids[:,j]=minJ+rangeJ*random.rank(k,1)
    return centroids

def kMeans(dataSet,k,distMeans=distEclud,createCent=randCent):
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2)))
    centroids=createCent(dataSet,k)
    clusterChange=True
    while clusterChange:
        clusterChange=False
        for i in range(m):
            minDist=inf
            minIndex=-1
            for j in range(k):
                distJI=distMeans(centroids[j,:],dataSet[i,:])
                if distJI<minDist:
                    minDist=distJI
                    minIndex=j
            if clusterAssment[i,0]!=minIndex:
                clusterChange=True
            clusterAssment[i,:]=minIndex,minDist**2
        print(centroids)
        for cent in range(k):
            ptsInClust=dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:]=mean(ptsInClust,axis=0)
    return centroids,clusterAssment

def show(dataSet,k,centroids,clusterAssment):
    from matplotlib import pyplot as plt
    numsamples,dim=dataSet.shape
    mark=['or','ob','og','ok','r','+r','sr','dr','<r','pr']
    for i in range(numsamples):
        markIndex=int(clusterAssment[i,:])
        plt.plot(dataSet[i,0],dataSet[i,1],mark[markIndex])
    mark=['Dr','Db','Dg','Dk','b','+b','sb','db','<b','pb']
    for i in range(k):
        plt.plot(centroids[i,0],centroids[i,1],mark[i],marksize=12)
    plt.show()

def main():
    dataMat=mat(loadDataSet("E:\撸撸撸\T10I4D100K.txt"))
    myCentroids,clustAssing=kMeans(dataMat,4)
    print(myCentroids)
    show(dataMat,4,myCentroids,clustAssing)

if __name__=='__main__':
    main()
