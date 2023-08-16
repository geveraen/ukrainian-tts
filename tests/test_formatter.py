from ukrainian_tts.formatter import preprocess_text
import pytest


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Quality of life update", "кваліті оф ліфе юпдате"),
        ("Він украв 20000000 $", "він украв двадцять мільйонів доларів"),
        ("Він украв 20000000", "він украв двадцять мільйонів"),
        ("Він украв 1 $", "він украв один долар"),
        ("Він украв 2 $", "він украв два долари"),
        ("Він украв 2 ₴", "він украв дві гривні"),
        (
            "111 000 000 000 доларів державного боргу.",
            "сто одинадцять мільярдів доларів державного боргу.",
        ),
        (
            "11100000001 доларів державного боргу.",
            "одинадцять мільярдів сто мільйонів один доларів державного боргу.",
        ),
        (
            "10000$, 15000 корупціонерів",
            "десять тисяч доларів , п'ятнадцять тисяч корупціонерів",
        ),  # TODO: fix space before comma
        (
            "$10000, 15000 корупціонерів",
            "доларів десять тисяч, п'ятнадцять тисяч корупціонерів",
        ),  # fix order
        (
            "10000$ у еквіваленті борщових заправок",
            "десять тисяч доларів у еквіваленті борщових заправок",
        ),
        # this is wrong case, should be "це дев'ятнадцятирічне вино."
        # Implementing this, require to have proper parsing of words into the token stream
        # which reqiure reworking of current approach.
        ("це 19-річне вино.", "це дев'ятнадцять-річне вино."),
        ("10-30-40-50-5-9-5", "десять-тридцять-сорок-п'ятдесят-п'ять-дев'ять-п'ять"),
    ],
)
def test_formatter(text, expected):
    assert preprocess_text(text) == expected
