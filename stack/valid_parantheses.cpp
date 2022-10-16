#include<bits/stdc++.h>
using namespace std;

class Parantheses {
public:
    bool isValid(string s) {
        stack<char> mystack;
        for(int i=0;i<s.length();i++){
            if(mystack.empty()){
                mystack.push(s[i]);
                
            }
            else if ((mystack.top() == '(' && s[i] == ')')
                 || (mystack.top() == '{' && s[i] == '}')
                 || (mystack.top() == '[' && s[i] == ']')){
                mystack.pop();
            }
            else{
                mystack.push(s[i]);
            }
            
        }
        if(mystack.empty()){
            return true;
            
        }
        else{
            return false;
        }
    }
};
int main(){
  Parantheses p;
  string s="()[]{}";
  
  cout<<p.isValid(s);
  
  return 0;
}
