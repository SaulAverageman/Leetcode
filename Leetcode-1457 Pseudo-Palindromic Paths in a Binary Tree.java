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
    static int out;
    public boolean chk(int[] arr){
        int odd=0;
        for(int e:arr)
            odd+=e%2;
        
        return odd<=1;
    }
    public void go(TreeNode node,int[] arr){
        if (node==null)
            return;
        arr[node.val-1]+=1;
        if(node.left==null && node.right==null)
            if (chk(arr))
                Solution.out+=1;
        
        go(node.left,arr);
        go(node.right,arr);
        arr[node.val-1]-=1;
    }
    
    public int pseudoPalindromicPaths (TreeNode root) {
        int[] count=new int[9];
        Solution.out=0;
        go(root,count);
        return Solution.out;
        
    }
}
