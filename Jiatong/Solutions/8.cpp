class Solution {
public:
    int myAtoi(string str) {
        int state = 0;
        // state0 for start
        // state1 for pos
        // state2 for neg

        if (str == "-2147483648") return -2147483648;
        int res = 0;

        for(char a : str) {
            if (state == 0 && a == ' ') {
                continue;
            } else if (a == ' ') {
                break;
            }

            if (state == 0 && a == '+') {
                state = 1;
                continue;
            }

            if (state == 1 && a == '-') {
                return res;
            }

            if (state == 0 && a == '-') {
                state = 2;
                continue;
            }

            if (state == 2 && a == '+') {
                return res * -1;
            }

            if (state == 1 && a == '+') {
                return res;
            }

            if (state == 2 && a == '-') {
                return (res * -1);
            }

            if (a == '0' || a == '1' || a == '2' || a == '3' || a == '4' || a == '5' || a == '6' || a == '7' || a == '8' || a == '9') {
                if (state != 2) { state = 1;}
                if (res > INT_MAX / 10) {
                    if (state == 2) {
                        return -2147483648;
                    } else {
                        return 2147483647;
                    }
                }
                if (res == INT_MAX / 10) {
                    if (state == 2) {
                        if ((a - 48) <= 8) {
                            
                        } else {
                            return -2147483648;
                        }
                    } else {
                        if ((a - 48) <= 7) {
                            
                        } else {
                            return 2147483647;
                        }
                    }
                }
                res = res * 10 + (a - 48);
            }

            if (a != '+' && a != '-' && a != '0' && a != '1' && a != '2' && a != '3' && a != '4' && a != '5' && a != '6' && a != '7' && a != '8' && a != '9') {
                break;
            }

            
        }

        if (state == 2) {
            res = -1 * res;
        }

        return res;
    }
};
