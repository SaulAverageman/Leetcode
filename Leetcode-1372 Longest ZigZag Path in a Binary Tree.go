/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func longestZigZag(root *TreeNode) int {
    out:=0
    left,right:=dfs(root.Left,&out,"l")+1, dfs(root.Right,&out,"r")+1

    if left>out{
        out=left
    }

    if right>out{
        out=right
    }

    return out-1
}

func dfs(node *TreeNode,out *int,prev string)int{
    if node==nil{
        return 0
    }

    left,right:=dfs(node.Left,out,"l")+1, dfs(node.Right,out,"r")+1
    
    if *out<left{
        *out=left
    }

    if *out<right{
        *out=right
    }

    if prev=="l"{
        return right
    }
    return left
}
