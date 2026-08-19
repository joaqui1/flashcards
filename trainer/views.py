from django.http import JsonResponse
from django.shortcuts import render
from .cards import CARDS, MODULES, VERSION_INFO


def _module_stats():
    """Return presentation metadata without mutating the shared module catalog."""
    return [
        {
            **module,
            "card_count": sum(card["module"] == module["id"] for card in CARDS),
            "code_count": sum(
                card["module"] == module["id"] and bool(card["code"])
                for card in CARDS
            ),
        }
        for module in MODULES
    ]


def _deck_stats():
    return {
        "cards": len(CARDS),
        "module_count": len(MODULES),
        "with_code": sum(bool(card["code"]) for card in CARDS),
        "debugging": sum(card["kind"] == "debugging" for card in CARDS),
        "completion": sum(card["kind"] == "completar" for card in CARDS),
        "verdicts": sum(card["verdict"] is not None for card in CARDS),
    }


def home(request):
    return render(
        request,
        "trainer/home.html",
        {"modules": _module_stats(), "version": VERSION_INFO, "stats": _deck_stats()},
    )


def study(request):
    return render(
        request,
        "trainer/study.html",
        {"modules": _module_stats(), "version": VERSION_INFO, "stats": _deck_stats()},
    )


def about(request):
    return render(
        request,
        "trainer/about.html",
        {"modules": _module_stats(), "version": VERSION_INFO, "stats": _deck_stats()},
    )


def cards_api(request):
    module = request.GET.get("module")
    cards = CARDS
    if module and module != "all":
        cards = [card for card in CARDS if card["module"] == module]
    return JsonResponse({"cards": cards, "count": len(cards), "version": VERSION_INFO})


def meta_api(request):
    return JsonResponse(
        {"modules": _module_stats(), "version": VERSION_INFO, **_deck_stats()}
    )
