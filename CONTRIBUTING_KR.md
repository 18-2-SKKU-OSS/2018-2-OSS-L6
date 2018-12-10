# Conventions
## Coding
* 항상 tab을 사용합니다.
* LF 개행 문자를 사용합니다.
* 중괄호는 항상 새 줄에 작성합니다.
* C# 6/C# 7 문법을 가능할 때마다 사용합니다.
* MS C# 표준 naming conventions을 지킵니다.
* 예외 처리를 정확한 때에 사용합니다.

**Naming Conventions**
~~~
//non-private variable
variableName

//private variable
_variableName

//methods
MethodName

//parameters
parameterName

//Properties
PropertyName
~~~

## Commit
**Commit을 할 때에는 다음을 지키십시오.**  
* Commit log를 코드만큼 좋은 상태로 유지하십시오. 새로운 contributor가 가장 먼저 보는 것이기 때문입니다.

* 하나의 commit은 하나의 변화만을 표현합니다. Commit 메세지와 무관한 변화가 commit에 있어서는 안됩니다.

**Commit 메세지를 작성할 때에는 다음을 지키십시오.**
* Diffs를 최대한 깔끔하게 하십시오.

* 불필요한 개행을 피하십시오.

## Pull Request
* Pull Request를 할 때, 최신 master 위에 rebase 되어 있음을 확인하십시오.
* 간단한 변화(한두 줄의 코드)는 자유롭게 PR 해 주십시오.
* 간단하지 않은 변화에 대해서는 다음을 지켜 주십시오.

  * 기존의 issue에 대해 작업하는 경우, 작업 전에 comment를 남기고 승인을 기다리십시오.
  * Issue가 존재하지 않는 경우, 제안을 담은 issue를 작성한 뒤 승인을 기다리십시오.
  * [개발자 디스코드](https://discord.gg/hearthsim-devs)의 #hdt에 프로젝트를 제안한 뒤 승인을 기다리십시오.