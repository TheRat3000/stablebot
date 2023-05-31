# stablebot
Discord Bot basic



Discord-Bot Skript
Dieses Python-Skript ist ein einfacher Discord-Bot, der mithilfe der discord.py-Bibliothek entwickelt wurde. Es stellt einige nützliche Funktionen bereit, die Discord-Benutzern helfen können.



Funktionen
Begrüßt Benutzer mit dem Befehl !hallo.
Erlaubt Benutzern mit entsprechenden Berechtigungen, andere Benutzer mit dem Befehl !kick zu kicken.
Erlaubt dem Eigentümer des Bots, den Bot mit dem Befehl !stop zu beenden.


Installation
Stelle sicher, dass Python 3 auf deinem System installiert ist.
Installiere die discord.py-Bibliothek mit dem Befehl pip install discord.py.
Gehe zur Discord Developer-Website (https://discord.com/developers/applications) und erstelle eine neue Anwendung.
Erstelle einen Bot für deine Anwendung und kopiere den Token des Bots.
Ersetze 'DEIN_BOT_TOKEN' in der bot.run()-Anweisung im Skript durch den kopierten Bot-Token.


Verwendung
Starte das Skript mit dem Befehl python bot.py (oder python3 bot.py, abhängig von deiner Python-Installation).
Der Bot sollte nun online sein und auf Befehle in den Discord-Servern antworten, zu denen er hinzugefügt wurde.
Verwende den Befehl !hallo, um den Bot dazu zu bringen, "Hallo" zusammen mit dem Namen des Benutzers, der den Befehl aufgerufen hat, zu senden.
Benutzer mit den Berechtigungen "kick_members" können den Befehl !kick @Benutzername verwenden, um den angegebenen Benutzer zu kicken.
Der Eigentümer des Bots kann den Befehl !stop verwenden, um den Bot zu beenden.
Bitte beachte, dass der Bot-Besitzer den Befehl !stop verwenden kann, um den Bot zu beenden. Stelle sicher, dass der Bot-Besitzer-Check in der stop-Funktion angepasst wird, um deine eigene Discord-Benutzer-ID zu verwenden.

Anpassung
Du kannst dieses Skript anpassen und weitere Funktionen hinzufügen, um den Bot deinen Anforderungen anzupassen. Die discord.py-Dokumentation (https://discordpy.readthedocs.io/) bietet eine umfassende Anleitung zur Verwendung der Bibliothek und zur Erstellung fortschrittlicherer Discord-Bots.

Viel Spaß beim Experimentieren mit dem Discord-Bot-Skript! Bei weiteren Fragen oder Anpassungen kannst du dich an den Entwickler wenden oder in der discord.py-Community Unterstützung suchen.
