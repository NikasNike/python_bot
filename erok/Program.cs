using Newtonsoft.Json.Linq;

string url = "https://api.telegram.org/bot5278735722:AAFr2vv8Wo_bMViUTntyGACRSgo-nWdU1AM/getUpdate"; //getUpdate is sendMessage?chat_id=&text=я слежу is getme

HttpClient hc = new HttpClient();



while (true)
{
    string res = hc.GetStringAsync(url).Result;

    JObject resultReq = JObject.Parse(res);

    JToken result = resultReq["result"]!;

    foreach (JToken messege in result)
    {
        string fName = messege["message"]!["from"]!["first_name"]!.ToString();
        string txtMsg = messege["message"]!["text"]!.ToString();

        System.Console.WriteLine($"{fName}: {txtMsg}");
    }
    Thread.Sleep(1000);
}