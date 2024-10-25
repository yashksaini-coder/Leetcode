class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        String[] words1 = s1.split(" ");
        Map<String, Integer> map = new HashMap<>();
        for(String word: words1){
            map.put(word,map.getOrDefault(word,0)+1);
        }
        String[] words2 = s2.split(" ");
        for(String word: words2){
            map.put(word,map.getOrDefault(word,0)+1);
        }
        ArrayList<String> ans = new ArrayList<>();
        for(Map.Entry<String,Integer> mp: map.entrySet()){
            if(mp.getValue()==1){
                ans.add(mp.getKey());
            }
        }
        return ans.toArray(new String[0]);
    }
}