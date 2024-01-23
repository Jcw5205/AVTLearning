import Williams_James as Jc
import Sweeney_Gavin as Gavin
import Amin_Prachit as Prachit

def names():
    names = [Jc.name(),Prachit.name()]
    for name in names:
        try:
            print(name)
        except:
            print("incorrect upload")
if __name__ == "__main__":
    names()