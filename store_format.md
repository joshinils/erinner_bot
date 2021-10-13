speichere in ordner mit namen `id` des chats;  
name.json, wo name eindeutiger string ist, also zb `id` der nachricht



jede errinerung:
json mit:
 * `date` ab wann errinert werden soll
 * `last_errinerung` zum kontrollieren, ob notwendig neu erinnern nach intervall
 * `content` beschreibung worum errinert werden soll
 * `nerven`
   * `do_nerven` bool ob genervt werden soll
   * `nerv_intervall` in minuten wie oft genervt werden soll
 * `repeat`
   * `do_repeat` bool ob erinnerung wiederholt werden soll in zukunft
   * `interval` abstand in minuten wann neue errinerung erstellt werden soll
   * irgendwie an andere instanzen linken?
     * errinerung duplizieren für repeat?
     * wie wann welche duplikate löschen?
 * `is_active` bool ob aufgabe abgeschlossen, also ob nerven notwendig?
   * kann benutzt werden um auflistung offener aufgaben zu filtern
   * nerven abschalten, oder mittels `do_nerven = false` setzen?