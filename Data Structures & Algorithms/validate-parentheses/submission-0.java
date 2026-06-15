class Solution {
    public boolean isValid(String s) {

        Stack<Character> valid = new Stack<>();

        Map<Character, Character> closeOpen = new HashMap<>();

        closeOpen.put(')', '(');
        closeOpen.put('}', '{');
        closeOpen.put(']', '[');

        for (char c : s.toCharArray()) {
            if (closeOpen.containsKey(c)) {
                if (!valid.isEmpty() && valid.peek() == closeOpen.get(c)) {
                    valid.pop();
                } else {
                    return false;
                }
            }
            else {
                valid.push(c);
            }
        }

        return valid.isEmpty();


        
    }
}
