class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(final int[] a, final int[] b) {
                return a[0] - b[0];
            }
        });
        PriorityQueue<Integer> prioQ = new PriorityQueue<Integer>( // priority queue of end times
                intervals.length, new Comparator<Integer>() {
                    public int compare(Integer a, Integer b) {
                        return a - b;
                    }
                });
        prioQ.add(intervals[0][1]);
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] >= prioQ.peek()) { // put meeting in existing room
                prioQ.poll();
            }
            prioQ.add(intervals[i][1]); // updates if replacing old meeting, adds if new room assigned
        }
        return prioQ.size();
    }
}
