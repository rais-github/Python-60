class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        helper(new ArrayList<Integer>(),result,candidates,target,0);
        return result;
    }
    public void helper(ArrayList<Integer> temp,List<List<Integer>> result,int[] candidates,int target,int start){
        if(target < 0){
            return ;
        }else if(target == 0){
            result.add(new ArrayList<>(temp));
        }else{
            for(int i = start;i<candidates.length;i++){
                temp.add(candidates[i]);
                helper(temp,result,candidates,target-candidates[i],i);
                temp.remove(Integer.valueOf(candidates[i]));
            }
        }
    }
}
