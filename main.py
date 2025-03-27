import yt_dlp

def baixar_video_instagram(links):
    ydl_opts = {
        'outtmpl': 'downloads/%(id)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': False,
        'flat_playlist': False,
        'writeinfojson': False,
        'extract_flat': False,
        'geo_bypass': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'nooverwrites': False,
        'ignore_errors': True,
        'force_generic_extractor': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for link in links:
            link = link.strip()
            if not link:
                print("Link vazio. Ignorando...")
                continue

            try:
                print(f"Baixando conteúdo: {link}")
                ydl.download([link])
                print(f"Download concluído para: {link}")
            except Exception as e:
                print(f"Erro ao baixar o conteúdo {link}: {e}")

def main():
    print("Bem-vindo ao downloader de vídeos do Instagram.")

    while True:
        links_input = input("Insira os links separados por vírgula (Ou 's' para sair):\n").strip()

        if links_input.lower() == 's':
            print("Saindo do programa...")
            break

        links = [link.strip() for link in links_input.split(",")]
        baixar_video_instagram(links)

if __name__ == "__main__":
    main()
