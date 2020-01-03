from typing import List, Dict


def mock_get_200(*args, **kwargs):
    return MockResponse(200, article_list_1)


def mock_get_400(*args, **kwargs):
    return MockResponse(400, {"description": "Bad request message"})


def mock_get_404(*args, **kwargs):
    return MockResponse(
        404,
        {"description": "No articles exist for the provided yearmonth"}
    )


def mock_get_500(*args, **kwargs):
    return MockResponse(500, {"description": "Internal server error"})


def mock_get_200_short(*args, **kwargs):
    return MockResponse(200, article_list_2)


def mock_post_200(*args, **kwargs):
    return MockResponse(
        200,
        {"message": "Monthstat record successfully added"}
    )


def mock_post_400(*args, **kwargs):
    return MockResponse(400, {"description": "Bad request message"})


def mock_post_404(*args, **kwargs):
    return MockResponse(400, {"description": "Not found message"})


def mock_put_200(*args, **kwargs):
    return MockResponse(
        200,
        {"message": "Monthstat record successfully updated"}
    )


class MockResponse():
    status_code: int
    json_data: List[Dict[str, str]]

    def __init__(self, status_code, article_list) -> None:
        self.status_code = status_code
        self.json_data = article_list

    def json(self):
        return self.json_data


article_list_1 = [
 {
  "body": "En man i Dalarna har dömts till fängelse efter att ha misshandlat och kränkt sina barn och sin dåvarande hustru i flera års tid, skriver Dalarnas Tidningar. Barnen har i förhör berättat om upprepat våld och kränkningar i form av slag, örfilar, knuffar och glåpord. Enligt ett av barnen gjorde slagen extra ont då pappan hade en ring på sig. Kvinnan har berättat om hur mannen vid ett tillfälle tog strypgrepp på henne medan hon satt och ammade. Mannen har förnekat alla beskrivna händelser. Falu tingsrätt anser dock att kvinnans och barnens berättelser är trovärdiga och också får stöd av vittnesmål från personer utanför familjen, skriver DT. Mannen döms till ett och ett halvt års fängelse och ska också betala skadestånd till både kvinnan och barnen. ",
  "created_at": "2019-12-27T07:41:30.957851Z",
  "headline": "Tog strypgrepp när hustrun ammade",
  "article_id": "kJPbpk"
 },
 {
  "body": "Polisen har gripit en man som misstänks ligga bakom branden i Gustavsberg på Värmdö under söndagen. Det är en man i 50-årsåldern som greps på platsen som nu misstänks för mordbrand, rapporterar P4 Stockholm. ",
  "created_at": "2019-12-27T07:41:31.186936Z",
  "headline": "Man misstänks för branden i Gustavsberg",
  "article_id": "jdnbvL"
 },
 {
  "body": "Maltas premiärminister Joseph Muscat kommer att avgå till följd av den senaste utvecklingen kring mordet på journalisten Daphne Caruana Galizia. Beskedet kommer efter att tusentals människor protesterat på nytt i Valletta. Muscat tillkännager en tidsplan för att lämna ifrån sig makten i ett tv-sänt framträdande på söndagskvällen, rapporterar maltesiska medier och Reuters. Han kommer att be sitt Labourparti att inleda en process för att välja en ny ledare den 12 januari – och någon gång efter det avgå både som premiärminister och partiledare. – Det här är vad landet behöver i detta skede, säger Muscat. Trycket har ökat på Muscat de senaste veckorna, när utredningen av mordet på journalisten Daphne Caruana Galizia för två år sedan tagit nya kliv och flera regeringsföreträdare kommit att figurera i den. När tusentals människor marscherade genom huvudstaden Valletta på söndagen – skanderandes slagord mot korruption och \"maffiastyret\" – gick den mördade journalistens föräldrar och anhöriga i täten, rapporterar public service-kanalen TVM. Deras budskap var att Muscat stått i vägen för rättvisan i mordutredningen. Det var den 16 oktober 2017 som Daphne Caruana Galizia dödades när en bomb exploderade i hennes bil när hon satt i den. Tre personer som greps kort därpå anklagas för att ha placerat ut bomben och detonerat den, men frågan som kvarstår efter två år är vem som ville att de skulle mörda journalisten. I lördags anklagades den inflytelserika affärsmannen Yorgen Fenech formellt för att ha varit med och planerat mordet. Han är den enda som ställts inför rätta för det hittills. I samband med att Fenech greps förra veckan avgick Keith Schembri, premiärminister Muscats stabschef och \"högra hand\", samt turismministern Konrad Mizzi. Bägge har tidigare avslöjats med ljusskygga ekonomiska kopplingar till Fenech. Yorgen Fenech nekar till inblandning, säger att brottsutredningen är politiskt styrd och pekar ut Schembri som hjärnan bakom journalistmordet. Schembri greps kort efter sin avgång, men släpptes senare och sades inte längre vara intressant för utredningen. Premiärminister Muscat har kritiserats för att ha låtit Keith Schembri delta i slutna möten om mordutredningen även efter att Fenech gripits, trots att det då var känt att han och Fenech hade kopplingar. Melvin Theuma, en taxiförare som säger sig ha agerat mellanhand vid beställningen av mordet, har benådats av regeringen i en uppgörelse som innebär att han inom kort kommer att vittna. Han förekommer bland annat på bild med Keith Schembri, en bild som demonstranter lyfter fram på olika plakat. Medieuppgifter har i flera dagar gjort gällande att premiärminister Muscat är på väg att meddela sin avgång, men från hans håll var det länge tyst. Hans parti Labourpartiet uttryckte tidigare på söndagen att det hade fortsatt förtroende för honom. När den upprörda folkmassan passerade partihögkvarteret i Valletta bommades fönstren igen, skriver Times of Malta. En delegation från EU-parlamentet är på väg till Malta för att granska rättsväsendets oberoende och uppgifterna om korruption på högsta nivå. Malta är en del av Europa, konstaterar den nederländska EU-parlamentarikern Sophie in't Veld, som leder delegationen. \"Detta berör oss alla\", skriver hon på Twitter enligt Reuters. ",
  "created_at": "2019-12-27T07:41:31.376964Z",
  "headline": "Maltas premiärminister avgår efter mordhärva",
  "article_id": "xPzbMQ"
 },
 {
  "body": "Den man i 30-årsåldern som kraschade sin bil genom väggen till Vikingahallen i Märsta på lördagskvällen misstänks för mordförsök, enligt polisen. Mannen har anhållits som skäligen misstänkt för brottet. – I det utredningsarbetet som gjordes angående grov vårdslöshet i trafik och grovt rattfylleri kom det in uppgifter som gjorde att polisen lade till brottsrubriceringen försök till mord, säger polisens presstalesperson Towe Hägg till TT. Mannen greps återigen på söndagskvällen och anhölls senare som skäligen misstänkt, den lägre misstankegraden, för mordförsök. Polisen vill dock inte gå in på varför han misstänks för mordförsök. – Han ska förhöras på nytt, vi har teknikerna som ska undersöka idrottshallen. Det är ett utredningsarbete som fortsätter under kvällen, säger Hägg. Åklagarmyndigheten vill inte kommentera fallet. – Åklagaren vill inte bekräfta eller dementera någonting, de vill inte säga någonting om ärendet helt enkelt, säger kommunikationsdirektör Karin Rosander. Medieuppgifter om att Säkerhetspolisen skulle vara inkopplat i fallet dementeras av Gabriel Wernstedt vid myndighetens presstjänst. – Svaret på den frågan är nej, det är ett polisärende, säger Wernstedt. Mannen körde in bilen genom väggen till idrottshallen mitt under en pågående handbollsmatch i ungdoms-SM. Spelare, ledare och publik flydde för livet bort från spelplanen men ingen person skadades. Mannen greps, misstänkt för bland annat grovt rattfylleri. Han släpptes senare fri men greps åter på söndagskvällen i en lägenhet i Sigtuna. Rättad: I en tidigare version av texten angavs fel misstanke i rubriken. ",
  "created_at": "2019-12-27T07:41:31.51925Z",
  "headline": "Misstänks för mordförsök efter krasch i hall",
  "article_id": "vQdbnw"
 },
 {
  "body": "Motorvärmare som överhettats kan vara boven bakom de bilbränder som inträffade på Järntorget i Göteborg under söndagen, rapporterar P4 Göteborg. Bränderna i de två bilarna var släckta vid 18-tiden. Polisen misstänker att branden spridit sig från en bil till den andra. ",
  "created_at": "2019-12-27T07:41:31.605213Z",
  "headline": "Motorvärmare kan ha orsakat bilbrand på Järntorget",
  "article_id": "lAmb4e"
 },
 {
  "body": "Sms:en avslöjade den folkkära artisten. I polisförhör erkänner han tre köp av metamfetamin – och förklarar också de hemliga koderna. – Han lärde mig att man inte ska prata i klarspråk om droger i meddelandena. Det betyder alltså tre gram, säger artisten i förhör. Den folkkära artisten berättar om kodorden bakom knarkköpen i förhör med polisen. ”Tina” ”miss Turner”, ”T” och ”Ice” är, enligt artisten, olika slanguttryck för drogen metamfetamin, en starkt beroendeframkallande narkotika som båda kan rökas och injiceras. – Crystal meth, säger artisten i polisförhör på frågan vad ”miss Tina Turner” betyder. Artisten som tävlat i Melodifestivalen och har haft en lång artistkarriär med mängder av hits erkänner direkt i polisförhör. Han fälls därför genom strafföreläggande för att ha köpt metamfetamin vid tre tillfällen under våren 2019 och måste nu betala dagsböter på totalt 60 000 kronor för tre fall av ringa narkotikabrott. Artisten är en del av en större narkotikahärva där den misstänkta langaren har suttit häktad sedan slutet av juni. Artisten kunde spåras genom en stor mängd sms och textmeddelanden genom apparna Whatsapp och Imessage. I polisförhöret berättar artisten att han kommit i kontakt med langaren via en sociala medier-app. – Jag köpte inte alla gånger som vi pratade om det. Jag minns att vi pratade om att köpa ”Tina” när jag träffade honom, men också att det inte blev av alla gånger, säger han. Textmeddelandena i polisens bevisning är fyllda med kodord. I ett meddelande skriver han: ”Lika bra jag bokar bord för tre personer” följt av en leende emoji. För polisen förklarar artisten: – NN (den misstänkta langaren, reds anm) lärde mig att man inte ska prata i klarspråk om droger i meddelandena. Det betyder alltså tre gram ”Tina”. Hörde uttrycket ”Tina” i USA för cirka fem år sen. Vet inte vad det kommer ifrån. I England säger man ”Ice”. I sms:en pratas det också om ”John Blunds magiska sovstenar”, som artisten också tackar ja till efter att ha fått förklarat att det är ”sömnisar”. – Jag fick några sömntabletter som bonus. Det var som stilnoct, en liten tablett i en grön karta som man delade. Han sa att jag absolut inte fick ta hela, säger artisten i polisförhöret. – Det stämmer inte, sa han då. Nöjesbladet har sökt artisten upprepade gånger under fredagen. Åklagaren Carl Mellberg konstaterar dock att artisten redan har betalt sina böter. – Jag kan konstatera att det här strafföreläggandet är godkänt genom betalning den 26 november, säger han. ",
  "created_at": "2019-12-27T07:41:31.62209Z",
  "headline": "Schlagerstjärnans hemliga knarkkoder – erkänner i förhör",
  "article_id": "MRvaV5"
 },
 {
  "body": "Det blinkar, glittrar, låter och lyser från 28-årige William Kurts hus. I en månads tid har han pyntat bostaden för sina döttrars skull. – De tycker det är jättekul med julen, och det gör jag med, säger han. – De flesta som går eller åker förbi tycker att det är jättefint och trevligt. Det livar upp och ger julstämning och många stannar för att ta bilder, säger William Kurt till Aftonbladet. Vid ett tillfälle blev en förbipasserande så upprymd att han skrapade fälgarna mot trottoarkanten när han försökte filma huset. Grannen rakt över gatan har också pyntat ordentligt och det har inspirerat William Kurt. Men främst är pyntandet en tidig julklapp till hans två döttrar. – De tycker det är jättekul med julen, och det gör jag med. Det är jättekul när det glittrar och lyser, säger han. Huset inte bara lyser. Det låter också. På låg volym, för att inte störa grannarna, spelas julmusik dygnet runt.  Pyntandet har tagit William Kurt nästan en hel månad. Han började tidigt i november och blev klar först här om dagen. Nära och kära har fått hjälpa till att färdigställa allt. – Det var meckigt att få ljusnätet att fastna på taket. Det såg så enkelt ut när jag köpte det... Men nu sitter det där, säger William Kurt. Är det ingen granne som har klagat på ditt lysande hus? – Nej. Eller jo, någon enstaka kanske. Men man kan inte göra alla nöjda, och ska man klaga på julpyntet som gör mina döttrar glada så borde man nog hitta någonting bättre att klaga på. ",
  "created_at": "2019-12-27T07:41:31.640426Z",
  "headline": "Willams hus glittrar, lyser och låter",
  "article_id": "JowR08"
 },
 {
  "body": "Litteraturfestivalen ”Littralund”, med fokus på barn- och ungdomslitteratur, kommer samarbeta med Lomma kommun vid nästa års arrangemang, skriver Lokaltidningen. Lomma kommer i april i år få två författarbesök som riktar sig till barn. Anna Trudesson som är skolbibliotekarie i kommunen hoppas att intresset för litteratur nu kommer stärkas lokalt. – Det är jättekul att vi kopplas samman med ”Litteralund” som är landets största bokfestival för barn och unga, säger hon till tidningen. ",
  "created_at": "2019-12-27T07:41:31.947897Z",
  "headline": "Bokfestival från Lund tar sig till Lomma i vår",
  "article_id": "pLObnX"
 },
 {
  "body": "En ny studie hävdar att en stadig kaffekonsumtion kan minska risken för diabetes typ 2 och hjärt- och kärlsjukdomar.  ✓ Så mycket är för mycket ",
  "created_at": "2019-12-27T07:41:32.038146Z",
  "headline": "Forskare: Så mycket kaffe är hälsosamt",
  "article_id": "RRnadA"
 },
 {
  "body": "  Sedan förra måndagen pågår FN:s årliga klimattoppmöte, COP25. Mötet skulle från början hållas i Chile, men flyttades för någon månad sen hastigt till Madrid. En flytt som fick Greta Thunberg att med förvånande snabbhet hitta en båt med besättning villig att segla österut över Atlanten, i helt fel säsong, för att ta henne tillbaka till Europa och mötet.    ”Being to sea, it changes you”, sa den gästande kaptenen Nikki Henderson när båten i förra veckan anlände till Lissabons hamn för att lämna av Thunberg.   Jag håller med henne. Man blir förändrad av att spendera tre veckor till havs, nära inpå vågorna och en liten grupp andra människor. På samma sätt som man blir förändrad av att låta den samlade klimatforskningen sjunka in i medvetandet. Den är nu det gäller. För om det inte är nu, när koldioxidhalten i atmosfären är högre än på 800 000 år, som vi gemensamt kan förändras tillräckligt mycket för att hugga i och ställa om – så när?   Men att det pågår ett avgörande klimattoppmöte som berör hela världen märks inte direkt i Malmö. Jag frågar runt om det är någon som känner till något COP25-relaterat här i stan. Inga svar.  Jag deltar i Miljövetarprogrammets utvecklingsråd på Malmö Universitet, men ingen där har hört om att universitetet gör något särskilt för att uppmärksamma mötet.  Jag söker på universitetets hemsida. Noll träffar. Vidare till Länsstyrelsen Skånes hemsida som när jag slår in ”COP25” frågar om jag inte egentligen menar ”copy”.   På Malmö stads hemsida får jag en träff! En tio år gammal artikel om klimattoppmötet COP15 som hölls i Köpenhamn. Förutom de sedvanliga fredagsstrejkerna och några andra civil olydnads-aktioner ekar det bekymmersamt tomt.   För nog är det ett bekymmer när viktiga globala händelser inte uppmärksammas lokalt. Inte minst eftersom vi människor uppfattar att de saker vi ser och hör talas om ofta är viktiga och ökar vårt engagemang – en mekanism som kallas tillgänglighetsbias. Nej, det duger inte att ett avgörande möte går Malmöborna förbi. Som att detta inte rörde oss.   Tvärtom borde det vara en självklarhet för Malmöpolitikerna och Malmös miljöarbetande tjänstemän att tydliggöra kopplingarna mellan det lokala klimatarbetet och de europeiska och globala överenskommelser som träffas på de årliga klimattoppmötena.    Vi vet att en anledning till att för få ännu engagerar sig i klimatfrågan är att den upplevs som för abstrakt, svår för gemene man att påverka. Kopplingarna måste bli tydligare: vilka konkreta insatser behöver Malmöborna bidra med för att Malmö ska ligga i linje med Parisavtalet? Den viktiga artikel 6 som förhandlas under COP25 och som bland annat handlar om hur utsläppshandeln mellan länder ska få ske, hur kan dess utformning påverka internationella Malmöföretag? Om det inte blir tydligare hur det globala och lokala hänger ihop, hur ska vi då förstå att det är allvar?    Så, Malmö, se det här som en efterlysning: du som uppmärksammar COP25 på lokal nivå, du som är villig att tydliggöra hur klimatarbetet i Malmö påverkas av besluten på klimattoppmötet, träd fram! För det här duger inte. ",
  "created_at": "2019-12-27T07:46:06.555445Z",
  "headline": "”Malmö fattar inte att det är nu det gäller”",
  "article_id": "8mL4lW"
 }
]


article_list_2 = [
 {
  "body": "En 1 # man . i , Dalarna - har dömts till fängelse efter att ha",
  "created_at": "2019-12-27T07:41:30.957851Z",
  "headline": "Tog strypgrepp när hustrun ammade",
  "article_id": "kJPbpk"
 },
 {
  "body": "Polisen har gripit en man som misstänks ligga. 192737834 + - # % ",
  "created_at": "2019-12-27T07:41:31.186936Z",
  "headline": "Man misstänks för branden i Gustavsberg",
  "article_id": "jdnbvL"
 },
 {
  "body": "abc 123 data",
  "created_at": "2019-12-27T07:41:31.186936Z",
  "headline": "testar att lägga till lite ord ?",
  "article_id": "jdnbvL"
 }
]
