# Site Consultoria Fluxo

- **Versão 5 (22/10/2026) [versao Claude], ainda NÃO publicada.** Segue o Design System Fluxo v1 (`1_Marca/Design System - Fluxo/`) e usa só o conteúdo da apresentação v8. A v3 e a v4 estão em `99_ARQUIVO/Site_versoes_antigas/`.
- `index.html`: página inicial. As 6 práticas viraram caixas clicáveis que levam às páginas de detalhamento.
- `praticas/*.html`: uma página por prática (M&A, Estruturação e modelagem, Estratégia, Processos, IA para negócios, Controladoria), com visão geral, o que entregamos, números, quando faz sentido, quem conduz, como trabalhamos e links para as outras práticas.
- `assets/css/fluxo.css` e `assets/js/fluxo.js`: estilo e animações compartilhados por todas as páginas (as animações são desligadas para quem ativa "reduzir movimento" no sistema).
- `_fonte/build.py`: gera o `index.html` e as páginas de prática a partir de um único texto. Para mudar textos das práticas, edite a lista `P` e rode `python _fonte/build.py` dentro de `3_Site` (a pasta `_fonte` não é publicada pelo GitHub Pages).
- `assets/img/`: fotos do ensaio + logos (`logo-azul.png` para fundo branco, `logo-branca.png` para fundo azul).
- `assets/img/clientes/`: logos de clientes (`ppf.png` não é mais usado — cliente saiu da lista vigente; `inhire.png` foi extraído da apresentação v8).
- `assets/img/carreira/`: logos da trajetória do fundador (McKinsey, Newbay, Squadra Sports, Ambev, Esporte Clube Bahia, UFBA), extraídos da apresentação v8.
- Prévia local: `.claude/launch.json` na raiz da área sobe um servidor estático (`npx serve`) na porta 4173 para visualizar com os caminhos relativos funcionando.

## Publicação (GitHub Pages)
- Esta pasta (`3_Site/`) é um repositório git local com remoto em `https://github.com/abraganca1/fluxo-site` (branch `main`), publicado via GitHub Pages com domínio customizado (`CNAME` → www.consultoriafluxo.com.br).
- A autenticação com o GitHub é por **máquina**, não por arquivo: cada computador guarda sua própria credencial no Credential Manager do Windows (ou equivalente), que **não** sincroniza pelo OneDrive. `.git/config` (sincronizado) só guarda o endereço do repositório, não segredos.
- Identidade dos commits: `Consultoria Fluxo <alvaro@consultoriafluxo.com.br>` (configurada só neste repositório, não afeta outros projetos — vale nos dois computadores assim que o OneDrive sincronizar).
- Para publicar: `git add -A && git commit -m "..." && git push origin main` dentro de `3_Site/`.

### No computador do Álvaro (dono da conta `abraganca1`)
Não precisa de token. Na primeira publicação, o `git push` vai abrir uma janela do GitHub pedindo login — ele entra com a própria conta `abraganca1` uma vez, e a máquina lembra depois disso.

### No computador do Gabriel
Já configurado com um token fine-grained (escopo só deste repositório), guardado no Credential Manager — não fica em nenhum arquivo da pasta. Como essa máquina tem mais de uma conta GitHub salva, o `git push` pode abrir uma janela "Select an account" mesmo assim; para evitar isso, rode com a variável de ambiente `GCM_GITHUB_AUTHMODES=pat git push origin main`. Se ainda assim abrir a janela, feche-a e rode o push de novo (`taskkill /F /IM git-credential-manager.exe` fecha a janela travada) — às vezes é preciso tentar duas vezes.

## Ordem das seções (v5)
Capa · Quem somos (4 números) · Clientes · Práticas (6 caixas clicáveis → `praticas/`) · Abordagem (4 fases) · Formato dos projetos · Fundador · Contato.

## Decisões de adaptação (site vs. deck)
- Paleta e tipografia (Source Serif 4 / Albert Sans / Saira) do sistema do site foram **mantidas**, não trocadas pela fonte sans-serif genérica do PDF exportado — é o sistema de marca digital já validado.
- Textos de navegação, botões de CTA e o WhatsApp flutuante são elementos só do site (o deck não tem equivalente).

## Pendências antes de publicar
1. Números do "Quem somos" (+R$100M, +R$50M, +50, +10) já confirmados na apresentação v8 revisada pelo Álvaro.
2. Confirmar autorização dos clientes para exibir os logos (inclui o novo logo da Inhire).
3. Fotos com o ex-sócio (vitor*.jpg, conversa, reuniao, dupla, laptop, parceria) não são mais usadas e podem ir para 99_ARQUIVO.
4. Fonte: títulos em Source Serif 4, textos em Albert Sans, rótulos em Saira (todas gratuitas, Google Fonts). A Prometo da pasta de marca é versão Trial.
5. Hospedagem do domínio consultoriafluxo.com.br (Netlify, Vercel, Hostinger…): basta subir esta pasta.
