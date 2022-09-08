/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private boolean go(TreeNode node,int par,int limit){
        if(node==null)
            return false;
        
        if(node.left==null && node.right==null)
            return node.val+par>=limit;
        boolean l=go(node.left,par+node.val,limit),r=go(node.right,par+node.val,limit);
        
        if(l==false)
            node.left=null;
        if(r==false)
            node.right=null;
        return l|| r;
    }
    
    public TreeNode sufficientSubset(TreeNode root, int limit) {
        if(go(root,0,limit))
            return root;
        return null;
        
    }
}
