func longestCycle(edges []int) int {
    vis:=make([]int,len(edges))
    dis:=make([]int,len(edges))
    out:=-1
    for i:=0;i<len(edges);i++{
        if vis[i]!=0{
            continue
        }
        route:=0
        j:=i
        prev:=-1
        for j!=-1 && vis[j]==0{
            vis[j]=i+1
            route+=1
            dis[j]=route
            prev=j
            j=edges[j]
        }
        
        if j!=-1 && vis[i]==vis[j]{
            //fmt.Println(j,prev)
            if out<dis[prev]-dis[j]+1{
                out=dis[prev]-dis[j]+1
            }
        }
    }
    //fmt.Print(vis,dis)
    return out
}
