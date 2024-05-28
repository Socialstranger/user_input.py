from _typeshed import Incomplete

import _win32typing
from win32.lib.pywintypes import TimeType, error as error

def InternetSetCookie(url: str, lpszCookieName: str, data: str, /) -> None: ...
def InternetGetCookie(Url: str, CookieName: str, /) -> str: ...
def InternetAttemptConnect(Reserved: int = ..., /) -> None: ...
def InternetCheckConnection(Url: str, Flags: int = ..., Reserved: int = ..., /) -> None: ...
def InternetGoOnline(Url: str, Parent: Incomplete | None = ..., Flags: int = ..., /) -> None: ...
def InternetCloseHandle(handle: _win32typing.PyHINTERNET, /) -> None: ...
def InternetConnect(
    Internet: _win32typing.PyHINTERNET,
    ServerName: str,
    ServerPort,
    Username: str,
    Password: str,
    Service,
    Flags,
    Context: Incomplete | None = ...,
) -> None: ...
def InternetOpen(agent: str, proxyName: str, proxyBypass: str, flags) -> None: ...
def InternetOpenUrl(
    Internet: _win32typing.PyHINTERNET, Url: str, Headers: str | None = ..., Flags: int = ..., Context: Incomplete | None = ...
) -> _win32typing.PyHINTERNET: ...
def InternetCanonicalizeUrl(url: str, flags: int = ..., /) -> str: ...
def InternetGetLastResponseInfo() -> tuple[Incomplete, str]: ...
def InternetReadFile(hInternet: _win32typing.PyHINTERNET, size, /) -> str: ...
def InternetWriteFile(File: _win32typing.PyHINTERNET, Buffer: str, /): ...
def FtpOpenFile(
    Connect: _win32typing.PyHINTERNET, FileName: str, Access, Flags, Context: Incomplete | None = ...
) -> _win32typing.PyHINTERNET: ...
def FtpCommand(
    Connect: _win32typing.PyHINTERNET, ExpectResponse, Flags, Command: str, Context: Incomplete | None = ...
) -> _win32typing.PyHINTERNET: ...
def InternetQueryOption(hInternet: _win32typing.PyHINTERNET, Option, /): ...
def InternetSetOption(hInternet: _win32typing.PyHINTERNET, Option, Buffer, /) -> None: ...
def FindFirstUrlCacheEntry(SearchPattern: Incomplete | None = ...) -> tuple[_win32typing.PyUrlCacheHANDLE, Incomplete]: ...
def FindNextUrlCacheEntry(EnumHandle: _win32typing.PyUrlCacheHANDLE): ...
def FindFirstUrlCacheEntryEx(
    SearchPattern: Incomplete | None = ..., Flags: int = ..., Filter: int = ..., GroupId=...
) -> tuple[_win32typing.PyUrlCacheHANDLE, Incomplete]: ...
def FindNextUrlCacheEntryEx(EnumHandle: _win32typing.PyUrlCacheHANDLE): ...
def FindCloseUrlCache(EnumHandle: _win32typing.PyUrlCacheHANDLE) -> None: ...
def FindFirstUrlCacheGroup(Filter=...) -> tuple[_win32typing.PyUrlCacheHANDLE, Incomplete]: ...
def FindNextUrlCacheGroup(Find: int): ...
def GetUrlCacheEntryInfo(UrlName): ...
def DeleteUrlCacheGroup(GroupId, Attributes=...) -> None: ...
def CreateUrlCacheGroup(Flags: int = ...): ...
def CreateUrlCacheEntry(UrlName, ExpectedFileSize, FileExtension): ...
def CommitUrlCacheEntry(
    UrlName,
    LocalFileName,
    CacheEntryType,
    ExpireTime: TimeType | None = ...,
    LastModifiedTime: TimeType | None = ...,
    HeaderInfo: Incomplete | None = ...,
    OriginalUrl: Incomplete | None = ...,
): ...
def SetUrlCacheEntryGroup(UrlName, Flags, GroupId) -> None: ...
def GetUrlCacheGroupAttribute(GroupId, Attributes=...): ...
def SetUrlCacheGroupAttribute(GroupId, Attributes, GroupInfo, Flags=...) -> None: ...
def DeleteUrlCacheEntry(UrlName, /) -> None: ...
def WinHttpGetDefaultProxyConfiguration(*args): ...  # incomplete
def WinHttpGetIEProxyConfigForCurrentUser(*args): ...  # incomplete
def WinHttpGetProxyForUrl(*args): ...  # incomplete
def WinHttpOpen(*args): ...  # incomplete

UNICODE: int
