#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char Domande[256];
    char Opzioni[3][256];
    int opzionicorrette;
} Domande;

void menu() {
    printf("Benvenuto al quiz sul mondo degli hacker!\n");
    printf("Scegli un'opzione:\n");
    printf("A) Iniziare una nuova partita\n");
    printf("B) Esci dal gioco\n");
}

char sceltauser() {
    char scelta;
    printf("Inserisci la tua scelta: ");
    scanf(" %c", &scelta);
    return scelta;
}

void iniziagioco() {
    Domande Domande[] = {
        {"Qual è il famoso gruppo di hacker noto per le loro operazioni di hacking a livello globale?",
         {"LulzSec", "Anonymous", "The Shadow Brokers"}, 1},
        {"Quale famoso hacker è conosciuto per aver violato i sistemi di diverse grandi aziende tecnologiche negli anni '80 e '90?",
         {"Kevin Mitnick", "Gary McKinnon", "Adrian Lamo"}, 0},
        {"Quale tecnica di hacking prevede l'uso di email false per ingannare le persone e ottenere informazioni sensibili?",
         {"SQL Injection", "Phishing", "Man-in-the-Middle"}, 1}
    };
        int num_Domande = sizeof(Domande) / sizeof(Domande[0]);

        char nomegiocatore[256];
        printf("Inserisci il tuo nome: ");
        scanf("%s", nomegiocatore);

        int punteggio = 0;
    for (int i = 0; i < num_Domande; i++) {
        printf("\nDomanda %d: %s\n", i + 1, Domande[i].Domande);
        for (int j = 0; j < 3; j++) {
            printf("%d) %s\n", j + 1, Domande[i].Opzioni[j]);
        }
        int Risposta;
        printf("Inserisci il numero della tua risposta: ");
        scanf("%d", &Risposta);
        if (Risposta - 1 == Domande[i].opzionicorrette) {
            printf("Risposta corretta!\n");
            punteggio++;
        }
            printf("Risposta sbagliata.\n");
        }

        printf("\n %s,hai totalizzato un punteggio di %d su %d.\n ",nomegiocatore,punteggio,num_Domande );
    }
    int main() {
    while (1) {
        menu();
        char scelta = sceltauser();
        if (scelta == 'A' || scelta == 'a') {
            iniziagioco();
        } else if (scelta == 'B' || scelta == 'b') {
            printf("GAME OVER.\n");
            break;
        } else {
            printf("Scelta non valida. Riprova.\n");
        }
    
    }
    
    return 0;
}


