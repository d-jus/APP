# WSTĘP (cel aplikacyjny)
**Ocena zagrożenia zawałowego <br>
dla polskich kopalń rud miedzi** <br>
*z wykorzystaniem Sztucznych Sieci Neuronowych*

*Heurystyka w moim rozumieniu to uproszczone, zdroworozsądkowe
zasady, dzięki którym łatwo zrealizować pewne założenia.
Jednakże ich główną zaletą jest to, że użytkownik wie, iż nie
są doskonałe i stanowią tylko środki doraźne, dzięki czemu nie wierzy
bezgranicznie w ich moc. Kiedy o tym zapominamy, stają się
niebezpieczne.* <br> Nassim Nicholas Taleb

`Ocena zagrożenia zawałowego z wykorzystaniem Sztucznych Sieci Neuronowych` to metoda opracowana w polskich kopalniach rud miedzi przy współudziale inżynierów górniczych. 

Cechy:
* **Kompleksowe łączenie informacji**
Ocena wykonywana jest na podstawie danych i informacji zebranych przez inżynierów w wyrobiskach dołowych oraz wyników badań laboratoryjnych. Otrzymywana jest na podstawie 16 czynników, klasycznie indywidualnie interpretowanych 
* **Współpraca działów**
16 czynników jest wyznaczanych przez pracowników działów: górniczych, geologicznych i tąpań, co umożliwia ich komunikację
* **Efektywność**
Ocena jest wykonywana z wykorzystywaniem danych już zbieranych przez zakłady górnicze
* **Możliwość wykonania oceny wielu wyrobisk**
Szybkość wyznaczenia wymaganych danych umożliwia wykonanie oceny wielu skrzyżowań w ciągu zmiany
* **Umożliwia porównanie warunków w rożnych rejonach**
Wskaźniki `CRF-m` i `CRF-p` umożliwiają porównanie cech górotworu w różnych rejonach
* **Stanowi pamięć zaistniałych zdarzeń**
Dane wykorzystane do zbudowania zbioru uczącego, stanowią „pamięć” zaistniałych zdarzeń
* **Jest narzędziem wsparcia decyzji**
Sugerowane działania dla wskaźników `CRF-m` i `CRF-p` stanowią wsparcie przy podejmowaniu decyzji przez inżynierów

W momencie opracowania `Oceny zagrożenia …` , polskie ośrodki badawcze nie oferowały podobnej metody, opartej na inżynierskiej ocenie cech górotworu  oraz Sztucznych Sieciach Neuronowych (dalej – SSN). Metoda została opracowana na podstawie badań wykonanych w zakładach górniczych KGHM Polska Miedź S.A, po których zostało potwierdzone istnienie zależności między ocenianymi czynnikami i postulowanymi bezwymiarowymi wskaźnikami: `CRF-p predyspozycja` i `CRF-m możliwość utrzymania`. Ukończone badania potwierdziły również możliwość opisania tych zależności z zastosowaniem SSN. Prace nad metodą były prowadzone mając na celu zapewnienie jej charakteru badawczego, poznawczego i użytecznego. Podejście to, umożliwiło opracowanie aplikacji desktopowej, **jednak jego profesjonalne użycie, wymaga jej dostosowania do indywidualnych potrzeb użytkowania.**

Metoda została opracowana w celu ograniczenia liczby niebezpiecznych zdarzeń, związanych z opadającymi masami skalnymi w kopalniach Legnicko - Głogowskiego Okręgu Miedziowego. Zagrożenie zawałami kształtowane jest przez grupę czynników, które występując, zwiększają prawdopodobieństwo utraty stateczności stropu. Relacje pomiędzy czynnikami a prawdopodobieństwem są nieznane.  Do ich znalezienia została użyta Sztuczna Sieć Neuronowa, która wymagała podania danych wejściowych oraz wyjściowych, stanowiących zbiór uczący. Podstawą opracowanej metody była tezę, iż ocena warunków geologicznych, górniczych i technicznych pozwala na dobór czynników kształtujących zagrożenie zawałami oraz na opracowanie miarodajnego wskaźnika oceny. <br>
Na podstawie wykonanych ocen warunków geologiczno - górniczych w wybranych wyrobiskach, badań endoskopowych oraz analiz danych archiwalnych zaistniałych zawałów, został utworzony zbiór par uczących SSN. Wykonane symulacje sieci neuronowych umożliwiły zaproponowanie nowej koncepcji oceny zagrożenia obwałami i opadem skał stropowych w kopalniach LGOM.

W wyniku przeprowadzonych obliczeń SSN, otrzymywane są dwa bezwymiarowe wskaźniki określające:
- predyspozycję danego fragmentu masywu skalnego do niszczenia, przemieszczeń i odkształceń `CRF-p` (dalej – *predyspozycja*),
- predyspozycję oraz możliwość utrzymania wyrobiska `CRF-m` (dalej – *możliwość utrzymania*)

# APLIKACJA 
#### (wersja przed refactoringiem)

Pierwotna wersja aplikacji desktopowej, został ukończona w sierpniu 2020 r. Jest ona zawarta w pliku `Prognoza zagrożenia zawałami - KGHM v.1.1.exe`. Kod źródłowy wersji `1.1` znajduje się w pliku `base_code.py`.

Pierwotna wersja aplikacji została wykonana jako wersja MVP. <br>
*MVP - wersja zaprojektowana bez dodatkowych, generujących koszty funkcjonalności.* <br>

Chodziło o to, by zbadać przy relatywnie niskim koszcie, czy produkt ma szansę na pozytywny odbiór użytkowników.<br>

**Dlaczego uważałem, że warto było opracować wersję MVP?**<br>

W fazie MVP mogło okazać się, że dalszy rozwój programu powinien być inny niż zaplanowany, bo użytkownicy zgłaszając swoje uwagi mogli wpłynąć na wprowadzenie nieprzewidzianych zmian (obsługa przez wielu użytkowników, centralna baza danych, wizualizacja wyników itp.)

# APLIKACJA 
#### (wersja po refactoringu)

Aplikacja w pierwotnej formie miała kilka wad, które należy poprawić przed dalszym rozwojem aplikacji.

Zasadniczym problemem jest płaska budowa kodu źródłowego.

plik `base_code.py` zawiera zarówno **logikę warstwy graficznej aplikacji**, **warstę obliczeń matematycznych** oraz **warstwę obsługi "bazy danych"**, która została rozdzielona.

Refactoring zatem ma na celu zwiększenie czytelności aplikacji.


