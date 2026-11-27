/*  SAMZLAB apps - add a new app by copying one block below. Nothing else to change.
    status: "live"  -> shows "Get it on Google Play"
            "soon"  -> shows "Coming soon" (closed testing / not published yet)
    package: the Play Store package name (the id= part of the Play link)            */
window.SAMZLAB_APPS = [
  {
    name: "Rimota: TV Remote & Mirror",
    short: "Rimota",
    package: "com.samz.rimota",
    status: "soon",
    icon: "assets/img/rimota.png",
    tagline: "Remote for every screen.",
    description: "A fast, beautiful remote for Android TV, Google TV and Android boxes - with screen mirroring, apps, files and a PC remote. No account, no ads, no cloud.",
    tags: ["Android TV", "Screen mirror", "PC remote", "Free + Pro"],
    privacy: "privacy/rimota/",
    terms: "terms/rimota/"
  },
  {
    name: "LanGuard Pro: OpenWrt Tools",
    short: "LanGuard Pro",
    package: "com.samz.languardpro",
    status: "live",
    icon: "assets/img/languardpro.png",
    tagline: "Your OpenWrt router, in your pocket.",
    description: "Manage OpenWrt and ImmortalWrt routers from Android: live traffic, connected devices, Wi-Fi, LuCI dashboard, speed tests, Wake-on-LAN and Tailscale.",
    tags: ["OpenWrt", "ImmortalWrt", "Router tools", "Free + Plus + Pro"],
    privacy: "privacy/languardpro/"
  }
];
window.SAMZLAB_EMAIL = "samzlabpk@gmail.com";
