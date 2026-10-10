class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();
        for (String word : words ){
            TrieNode current = root;
            for (char c : word.toCharArray()) {
                int index = c - 'a';
                if (current.children[index] == null) {
                    current.children[index] = new TrieNode();
                }
                current = current.children[index];
            }
            current.word = word;
        }
        List<String> result = new ArrayList<>();
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[r].length; c++) {
                dfs(r, c, root, board, result);
            }
        }
        return result;
    }
}

class TrieNode {
    TrieNode[] children = new TrieNode[26];
    String word = null;
}
private void dfs(int r, int c, TrieNode node, char[][] board, List<String> result) {
    if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] == '#') {
        return;
    }
    int index = board[r][c] - 'a';
    if (node.children[index] == null) {
        return;
    }
    
    TrieNode child = node.children[index];
    if (child.word != null) {
        result.add(child.word);
        child.word = null;
    }
    
    char temp = board[r][c];
    board[r][c] = '#';
    
    dfs(r + 1, c, child, board, result);
    dfs(r - 1, c, child, board, result);
    dfs(r, c + 1, child, board, result);
    dfs(r, c - 1, child, board, result);
    
    board[r][c] = temp;
}


