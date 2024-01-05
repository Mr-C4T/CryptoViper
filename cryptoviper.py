import os
import subprocess
import argparse

def main():
  # Art ASCII 
  snake_ascii = """
                                                                                
                          \x1b[1;32m39493                                              
                     799917999999997                                         
                   759999 1 697949969                                        
                  699999997   297997997      35997999                        
                  993979         959997    939919929999                      
                 352996           999991  652765 119691                      
                 799993          992999  95559   749994                     
        699799   9 99299         79969  99991    99967                      
      777   799   2991999       699699  3939 7   99294      1312              
    93      7599    4399991      6699    49571    577 12163999359694        
             929      39793    791959    399193    9779997696\033[95m( 0)\x1b[1;32m9597       
             993       91995  699692      96996           529993607        
             9497      69477  494993       99924               \033[95mV  V  \x1b[1;32m       
             71999    34593  313993        9555                             
              599935199991   739627       19691                             
                 7742299      9995972   9599697   \033[95m                           
 _____  \x1b[1;32m                       959919599799996 \033[95m                 _____            
( ___ ) \x1b[1;32m                        7461 9999969 \033[95m                  ( ___ )                   
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[1;32m793919\033[95m~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |\x1b[1;32m                                                          \033[95m|   | 
 |   |\x1b[1;32m  ____ ____ _   _ ___  ___ ____    _  _ _ ___  ____ ____  \033[95m|   | 
 |   |\x1b[1;32m  |    |__/  \_/  |__]  |  |  |    |  | | |__] |___ |__/  \033[95m|   | 
 |   |\x1b[1;32m  |___ |  \   |   |     |  |__|     \/  | |    |___ |  \  \033[95m|   | 
 |   |\x1b[1;32m                                                          \033[95m|   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                        (_____)
"""
  print("\033[95m" + snake_ascii + "\x1b[1;32m")

  parser = argparse.ArgumentParser(description="Automated WPA2 handshakes processing and cracking with hcxpcapngtool and hashcat")
  parser.add_argument("--process", action="store_true", help="Processing pcap folder")
  parser.add_argument("--crack",action="store_true", help="Cracking hash folder")
  parser.add_argument("--wordlist",default="wordlist/rockyou.txt",help="Wordlist file path")
  parser.add_argument("--input",default="pcap/",help="pcap folder path")
  parser.add_argument("--hash",default="hashfile/",help="hash folder path")
  parser.add_argument("--loot",default="loot/",help="loot folder path")
  parser.add_argument("--hashcat",default="hashcat",help="hashcat path")


  args = parser.parse_args()

  input_folder = args.input
  hash_folder = args.hash
  loot_folder = args.loot

  if args.process:  
    # Liste tous les fichiers pcap dans le dossier d'entrée
    pcap_files = [f for f in os.listdir(input_folder) if f.endswith("cap")]

    for pcap_file in pcap_files:
      print("\033[95m\nCAPTURE FILE : ",pcap_file,"\x1b[1;32m\n")
      input_path = os.path.join(input_folder, pcap_file)
      output_file = os.path.splitext(pcap_file)[0] + ".hc22000"
      output_path = os.path.join(hash_folder, output_file)

      # Utilise subprocess pour appeler hcxpcapngtool depuis la ligne de commande
      subprocess.run(["hcxpcapngtool", "-o", output_path,input_path])

  if args.crack:
    hash_files = [f for f in os.listdir(hash_folder) if f.endswith(".hc22000")]

    for hash_file in hash_files:
      print("\033[95m\nHASH FILE : ",hash_file,"\x1b[1;32m\n")
      hashcat_input_path = os.path.join(hash_folder, hash_file)
      hashcat_output_file = os.path.splitext(hash_file)[0] + ".txt"
      hashcat_output_path = os.path.join(loot_folder,hashcat_output_file)
      # Lance hashcat sur le fichier généré par hcxpcaptool
      subprocess.run([args.hashcat, "-m", "22000","-w","3","-o",hashcat_output_path,hashcat_input_path, args.wordlist])
      print("\033[95m\nLOOT FILE : ",hashcat_output_file,"\x1b[1;32m\n")

if __name__ == "__main__":
    main()