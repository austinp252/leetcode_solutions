class Solution {
    public int countPrimes(int n) { // O(n^2)
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (isPrime(i)) {
                count++;
            }
        }
        return count;
    }

    public boolean isPrime(int n) { // O(n)
        double root = Math.floor(Math.pow(n, 0.5)); // get root of n
        if (n <= 1)
            return false;
        else {
            for (int i = 2; i <= root; i++) {
                if (n % i == 0) {
                    return false;
                }
            }
        }
        return true;
    }
}