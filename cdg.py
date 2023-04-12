def cout_complet(cd, cid):
    """
    cd = charges directes
    cid = charges indirectes
    """
    return cd + cid

def cout_uo(cid, nb_uo):
    """
    cid = charges indirectes
    nb_uo = nombre d'unite d'oeuvre, euros pour assiette de frais
    """
    return cid / nb_uo

def stock_final_theorique(si, e, s):
    """
    si = stock initial
    e = entrees
    s = sorties
    """
    return si + e - s

def cout_achat(pa, ch):
    """
    pa = prix d'achat
    ch = charges liees
    """
    return pa + ch

def cmup(siv, ev, siq, eq):
    """
    siv = stock initial en valeur
    ev = entrees en valeur
    siq = si quantite
    eq = e en q
    """
    return (siv + ev) / (siq + eq)

def cout_prod(cmp, cdp, cidp):
    """
    cmp = cout matieres premieres
    cdp = charges directes production
    cidp = charges indirectes production
    """
    return cmp + cdp + cidp

def cout_revient(cp, chp):
    """
    cp = cout production
    chp = cout hors production
    """
    return cp + chp

def res_prod_vendu(ca, cr):
    """
    ca = chiffre d'affaire ou prix de vente
    cr = cout revient
    """
    return ca - cr

def section_homo(cid, uvt, up):
    """
    cid = charges indirectes totales
    uvt = unite vendues totales
    up = unite produit en question
    """
    charges = cid / uv
    return charges * up

def abc_cu(ct, nit):
    """
    ct = cout total
    nit = nombre inducteurs total
    """
    return ct / nit

def abc_ci(cui, ni):
    """
    cui = abc_cu ou cout unitaire inducteur
    ni = nombre inducteur en question
    """
    return cui * ni

def marge_cv(pvu, cvu):
    """
    pvu = prix vente unitaire ou ca
    cvu = cout vente unitaire ou cout variable
    """
    return pvu - cvu

def taux_marge_cv(mcv, ca):
    """
    mcv = marge cout variables
    ca = chiffre d'affaire
    """
    return mcv / ca

def res_entreprise(mcv, cf):
    """
    mcv = marge cout variable
    cf = charges fixes
    """
    return mcv - cf

def seuil_rent(cf, tmcv):
    """
    cf = charges fixes
    tmcv = taux marges cout variable
    """
    return cf / tmcv

def sr_q(cf, pu, cvu):
    """
    cf = charges fixes
    pu = prix vente unitaire
    cvu = cout variable unitaire
    """
    return cf / (pu - cvu)

def pm(sr, ca):
    """
    sr = seuil rentabilite
    ca = chiffre d'affaire
    """
    return sr * 365 / ca

def marge_secu(ca, sr):
    """
    ca = chiffre d'affaire
    sr = seuil rentabilite
    """
    return ca - sr

def indice_secu(ms, ca):
    """
    ms = marge securite
    ca = chiffre d'affaire
    """
    return ms * 100 / ca

def indice_prel(cf, ca):
    """
    cf = cout fixes
    ca = chiffre d'affaire
    """
    return cf * 100 / ca

def levier_operationnel(dr, r, dca, ca):
    """
    dr: variation du résultat
    r: résultat
    dca: variation du chiffre d'affaire
    ca: chiffre d'affaire
    ou 1 / indice_secu
    ou marge cout variable / resultat
    """
    return (dr / r) / (dca / ca)

def ecart_q(qr, qp, pup):
    """
    qr = quantite realisee
    qp = quantite prevue
    pup = prix unitaire prevu
    """
    return (qr - qp) * pup

def ecart_p(pr, pp, qr):
    """
    pr = prix unitaire realise
    pp = prix unitaire prevu
    qr = quantite realisee
    """
    return (pr - pp) / qr
