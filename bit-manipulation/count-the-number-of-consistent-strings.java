class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        Set<Character> set=new HashSet<>();
        for(int i=0;i<allowed.length();i++){
            set.add(allowed.charAt(i));
        }
        int count=0;
        for(String k:words){
            int flag=1;
            for(int i=0;i<k.length();i++){
                if(!set.contains(k.charAt(i))) {
                    flag=0;
                    break;
                }
            }
            count+=flag;
        }
        return count;
    }
}