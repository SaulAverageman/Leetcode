/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func widthOfBinaryTree(root *TreeNode) int {
    out:=0
    levels:=make([][]int,0)
    dfs(root,&levels,1,0,&out)
    return out+1
    
}

func dfs(node *TreeNode, levels *[][]int,depth int,width int,out *int){
    if node==nil{
        return
    }

    if len(*levels)<depth{
        *levels=append(*levels,[]int{math.MaxInt,math.MinInt})
    }
    if width<(*levels)[depth-1][0]{
        (*levels)[depth-1][0]=width
        //fmt.Println(1,node.Val,depth,levels[depth-1])
    }

    if width>(*levels)[depth-1][1]{
        (*levels)[depth-1][1]=width
        //fmt.Println(2,node.Val,depth,levels[depth-1])
    }

    if *out<(*levels)[depth-1][1]-(*levels)[depth-1][0]{
        *out=(*levels)[depth-1][1]-(*levels)[depth-1][0]
    }

    dfs(node.Left,levels,depth+1,2*width,out)
    dfs(node.Right,levels,depth+1,2*width+1,out)

}
