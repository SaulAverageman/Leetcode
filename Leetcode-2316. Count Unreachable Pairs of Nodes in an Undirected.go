func countPairs(n int, edges [][]int) int64 {
    paths:=make(map[int][]int)
    for _,e:=range(edges){
        paths[e[0]]=append(paths[e[0]],e[1])
        paths[e[1]]=append(paths[e[1]],e[0])
    }
    vis:=make([]int,n)
    var clusters []int
    for i:=0;i<n;i++{
        if vis[i]==0{
            clusterSize:=0
            dfs(i,&vis,paths,&clusterSize)
            clusters=append(clusters,clusterSize)
        }
    }
    var out int64

    for i:=1;i<len(clusters);i++{
        out+=int64(clusters[i]*clusters[i-1])
        clusters[i]+=clusters[i-1]
    }
    return out
}

func dfs(node int,vis *[]int,paths map[int][]int,clusterSize *int){
    (*vis)[node]=1
    (*clusterSize)+=1
    for _,next:=range(paths[node]){
        if (*vis)[next]==0{
            dfs(next,vis,paths,clusterSize)
        }
    }
}
