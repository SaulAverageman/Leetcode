class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        Queue<Integer> q=new PriorityQueue<>();
        q.add(-startFuel);
        int tank=0;
        int stops=-1;
        
        for (int[] arr: stations){
            while(tank<arr[0] && q.size()!=0){
                tank+=-q.poll();
                stops+=1;
            }
            if (tank<arr[0])
                return -1;
            q.add(-arr[1]);
        }
        
        while(tank<target && q.size()!=0){
            tank+=-q.poll();
            stops+=1;
        }
        if(tank<target)
            return -1;
        return stops;
    }
}
