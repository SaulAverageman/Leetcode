func minJumps(arr []int) int {
    ind:=make(map[int][]int)

    for i,e:=range(arr){
        ind[e]=append(ind[e],i)
    }
    dis:=make([]int,len(arr))
    vis:=make(map[int]bool)

    for i,_:=range(dis){
        dis[i]=100000
        vis[arr[i]]=false
    }

    q:=make([][]int, len(arr))

    q[0]=[]int{0,0}
    j:=1
    
    
    
    for i:=0;i<len(q);i++{
        e:=q[i]
        dis[e[0]]=e[1]
        
        if vis[arr[e[0]]]==false{
            for _,next:=range(ind[arr[e[0]]]){
                if next!=e[0]{
                    if dis[next]>e[1]+1{
                        dis[next]=e[1]+1
                        q[j]=[]int{next,e[1]+1}
                        j++
                    }
                }
            }
        }

        vis[arr[e[0]]]=true

        if e[0]-1>=0 && dis[e[0]-1]==100000{
            dis[e[0]-1]=e[1]+1
            q[j]=[]int{e[0]-1,e[1]+1}
            j++
        }

        if e[0]+1<len(dis) && dis[e[0]+1]==100000{
            dis[e[0]+1]=e[1]+1
            q[j]=[]int{e[0]+1,e[1]+1}
            j++
        }
    }
    
    
    return dis[len(dis)-1]
}
