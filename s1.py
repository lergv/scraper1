# import HTMLSession from requests_html
from requests_html import HTMLSession
import io

import re


if __name__ == '__main__':
    # create an HTML Session object
    session = HTMLSession()
    # Use the object above to connect to needed webpage
    #resp = session.get("https://finance.yahoo.com/quote/NFLX/options?p=NFLX")
    resp = session.get("https://www.sreality.cz/hledani/prodej/byty/praha")

    # Run JavaScript code on webpage
    resp.html.render()

##    f = open("demofile2.txt", "w")
##    f.write(resp.html.html)
##    f.close()



##    <p class="info ng-binding">
##		Zobrazujeme výsledky
##		<span class="numero ng-binding">1–20</span>
##		z celkem
##		<span class="numero ng-binding">4&nbsp;811</span>&nbsp;nalezených
##	</p>

    fname = "demofile2.html"
    
    with io.open(fname, "w", encoding="utf-8") as f:
        f.write(resp.html.html)

    #title =  resp.html.find('.numero', first=True).text
    title =  resp.html.find('.numero')[1].text.strip()
    title = re.sub("[^0-9]", "", title)
    print(title)
