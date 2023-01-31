function fct1(var9, var5) {
    const var10 = fct2();
    return fct1 = function(var11, var3) {
        var11 = var11 - (0x1889 + 0x1 * 0x1e2f + -0x34c6);
        let var14 = var10[var11];
        return var14;
    }, fct1(var9, var5);
}
const var8 = fct1;
(function(var7, var4) {
    const var2 = fct1,
        var13 = var7();
    while (!![]) {
        try {
            const var12 = -parseInt(var2(0x201)) / (0xd1f + -0x5d * -0x11 + -0x134b) * (-parseInt(var2(0x20d)) / (0xd84 + 0xa9 * 0x2c + -0x2a8e * 0x1)) + -parseInt(var2(0x1fa)) / (0x76a + 0x245 + -0x4 * 0x26b) * (parseInt(var2(0x1f7)) / (0xb8a * 0x2 + 0x194b + -0x1 * 0x305b)) + parseInt(var2(0x209)) / (0x1b2d + 0x1841 + -0x3369) + parseInt(var2(0x1fb)) / (0xf95 + 0x23d * -0x9 + 0x1 * 0x496) + parseInt(var2(0x20a)) / (-0x1 * -0x275 + -0x1920 + 0x16b2) * (parseInt(var2(0x205)) / (0x23d9 + 0x1bd * -0xe + -0xb7b)) + parseInt(var2(0x1f5)) / (-0x1547 + -0x6ee + 0x1 * 0x1c3e) + parseInt(var2(0x20b)) / (0x1 * -0x6b + 0x262f + -0x25ba) * (-parseInt(var2(0x202)) / (0x153e + -0xe6c + -0x6c7 * 0x1));
            if (var12 === var4) break;
            else var13['push'](var13['shift']());
        } catch (var1) {
            var13['push'](var13['shift']());
        }
    }
}(fct2, 0x51e39 + 0x14be8 + -0x2ba81));
let root1, root2, a = prompt(var8(0x1fe) + var8(0x1f9) + var8(0x1fd)),
    b = prompt(var8(0x1fe) + var8(0x1f8) + var8(0x208)),
    c = prompt(var8(0x1fe) + var8(0x1f2) + var8(0x1fd)),
    discriminant = b * b - (0xb3 * -0x2f + 0x3df * 0x7 + 0x5c8) * a * c;

function fct2() {
    const var6 = ['\x20-\x20', 'n\x20are\x20', '2069262zGNYXO', 'log', '38672SSqjRu', 'second\x20num', 'first\x20numb', '3bjNLlU', '1778400eSPIpM', 'i\x20and\x20', 'er:\x20', 'Enter\x20the\x20', '\x20and\x20', 'toFixed', '1519IrYSXV', '201091PyXaYG', '\x20+\x20', 'of\x20quadrat', '3112920YuYctb', 'The\x20roots\x20', 'ic\x20equatio', 'ber:\x20', '2022985WWEkBM', '7resypr', '750ZQCTNe', 'sqrt', '398EkNHEt', 'third\x20numb'];
    fct2 = function() {
        return var6;
    };
    return fct2();
}
if (discriminant > 0x407 * 0x7 + -0x1d70 + -0x13f * -0x1) root1 = (-b + Math[var8(0x20c)](discriminant)) / ((0x167f + 0x79 * 0x1f + 0x2524 * -0x1) * a), root2 = (-b - Math[var8(0x20c)](discriminant)) / ((0x25fa + -0x1f57 + -0x6a1) * a), console[var8(0x1f6)](var8(0x206) + var8(0x204) + var8(0x207) + var8(0x1f4) + root1 + var8(0x1ff) + root2);
else {
    if (discriminant == 0x76 * 0x21 + -0x1e84 + -0x3 * -0x51a) root1 = root2 = -b / ((0xb8c + -0xdb1 + -0x1d * -0x13) * a), console[var8(0x1f6)](var8(0x206) + var8(0x204) + var8(0x207) + var8(0x1f4) + root1 + var8(0x1ff) + root2);
    else {
        let realPart = (-b / ((0x87a + 0x1 * 0x8dd + -0x1155) * a))[var8(0x200)](-0x4 * 0x68d + 0x1785 + 0x2b1),
            imagPart = (Math[var8(0x20c)](-discriminant) / ((0x5 * -0x427 + 0x61 * 0x3b + 0x1 * -0x196) * a))[var8(0x200)](0xb * 0x10b + 0x5 * -0x5c9 + 0x37e * 0x5);
        console[var8(0x1f6)](var8(0x206) + var8(0x204) + var8(0x207) + var8(0x1f4) + realPart + var8(0x203) + imagPart + var8(0x1fc) + realPart + var8(0x1f3) + imagPart + 'i');
    }
}