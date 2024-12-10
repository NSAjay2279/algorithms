const MAX_LINES = 100;

shortest_line_index(var lines[], var n) {
    var j;
    var shortest = 0;
    for (j = 1; j < n; i++)
        if (lines[j] < lines[shortest])
            shortest = j;
    return shortest;
}

void solve(int lines[], int n, int m) {
    int i, shortest;
    for (i = 0; i < m; i++) {
        shortest = shortest_line_index(lines, n);
        console.log(lines[shortest]);
        lines[shortest]++;
    }
}

function main(void) {
    var lines[MAX_LINES];
    var n, m, i;
    
}
