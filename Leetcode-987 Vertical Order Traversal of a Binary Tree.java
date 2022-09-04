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
    static List<List<int[]>> out;
    static int min=0;
    static int max=0;
    public void go(TreeNode node,int ind,int height){
        if(node==null)
            return;
        if(ind<Solution.min){
            Solution.out.add(0,new ArrayList<>());
            Solution.min=ind;
        }
        
        if(ind>Solution.max){
            Solution.out.add(new ArrayList<>());
            Solution.max=ind;
        }
        
        Solution.out.get(ind-Solution.min).add(new int[]{height, node.val});
        go(node.left,ind-1,height+1);
        go(node.right,ind+1,height);
    }
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        Solution.out=new ArrayList<>();
        Solution.min=0;
        Solution.max=0;
        Solution.out.add(new ArrayList<>());
        go(root,0,0);
        
        for(int i=0;i<Solution.out.size();i++){
            Collections.sort(Solution.out.get(i), new Comparator<int[]>(){
               public int compare(int[] a,int[] b){
                   if (a[0]==b[0])
                       return Integer.compare(a[1],b[1]);
                   return Integer.compare(a[0],b[0]);
               } 
            });
        }
        
        
        List<List<Integer>> arr=new ArrayList<>();
        for(List<int[]> e : Solution.out){
            arr.add(new ArrayList<>());
            for(int[] ee:e)
                arr.get(arr.size()-1).add(ee[1]);
        }
        return arr;
    }
}
