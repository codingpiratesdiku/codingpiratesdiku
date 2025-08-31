/*
 Músico Nerd
 Theremin com LDR
 por Gustavo Silveira
 www.musiconerd.com

 */

const int ldrPin = A0;      // Pin of the photo resistor
const int speaker = 11;     // Pin of the speaker

int sensorValue = 0;        // The value read from the photo resistor
int LDR = 0;                // The value to play

int sensorMin = 42;         // The minimum value to read from the photo resistor
int sensorMax = 950;        // The maximum value to read from the photo resistor

int freqMin = 200;          // The minimum frequency (in Hz) to play using the pizo
int freqMax = 1200;         // The maximum frequency (in Hz) to play using the pizo


void setup() {
  // Inicializa a comunicação serial
  Serial.begin(9600);
}

void loop() {
  // Lê o avalor analógico do LDR
  sensorValue= analogRead(ldrPin);

  // mapeia os valores do LDR para as frequencias desejadas
 LDR = map(sensorValue, sensorMin, sensorMax, freqMin, freqMax);

  
  tone(speaker, LDR); // A Função tone é responsável por fazer o auto falante tocar a frequencia desejada - tone(pino, frequencia);

  // print the results to the serial monitor:
  Serial.print("sensor = ");
  Serial.println(sensorValue);

  delay(2); // espera 2 milisegundos 
}