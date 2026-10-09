class WordDictionary {

    public WordDictionary() {
    }
    TrieNode root = new TrieNode();
    public void addWord(String word) {
        TrieNode current = this.root;
        for (int i =0 ; i< word.length() ; i++) {
            char c = word.charAt(i);
            int index = c - 'a';
            if (current.children[index]== null){
                current.children[index] = new TrieNode();
            }
            current = current.children[index];
        }
        current.isEndOfWord = true;
    }


    public boolean search(String word) {
        
        return dfs(this.root, word, 0);
    }
    private boolean dfs(TrieNode node, String word, int wordIndex){
            if (wordIndex == word.length()){
                return node.isEndOfWord;
            }
            char c = word.charAt(wordIndex);
            if (c != '.'){
                int index = c - 'a';
                if (node.children[index] == null){
                    return false;
                }
                else {
                    return dfs(node.children[index], word, wordIndex + 1);
                }
            }
            else {
                for (int i = 0 ; i<26 ; i ++){
                    if (node.children[i]!= null){
                        if (dfs(node.children[i], word, wordIndex + 1)) {
                            return true;
                        }
                    }
                }
                return false ;

            }
        }
}
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEndOfWord = false;
}
