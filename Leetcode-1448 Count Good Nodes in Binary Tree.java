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
    public int count(TreeNode node,int max){
        if(node==null)
            return 0;
        if (node.val>=max)
            return 1+count(node.left,node.val)+count(node.right,node.val);
        return count(node.left,max)+count(node.right,max);
    }
    public int goodNodes(TreeNode root) {
        return count(root,Integer.MIN_VALUE);
    }
}
