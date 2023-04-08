/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
    vis:=map[int]*Node{}

    return cloneNode(node,vis)
}

func cloneNode(parent *Node, vis map[int]*Node) *Node{
    if parent==nil{
        return nil
    }
    
    child:=&(Node{
        Val : parent.Val,
        Neighbors : make([]*Node,len(parent.Neighbors)),
    })

    vis[parent.Val]=child

    for i,next:=range(parent.Neighbors){
        v,x:=vis[next.Val]
        if x{
            child.Neighbors[i]=v
        }else{
            child.Neighbors[i]=cloneNode(next,vis)
        }
    }
    return child
}
