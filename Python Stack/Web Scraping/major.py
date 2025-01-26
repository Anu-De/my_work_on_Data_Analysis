from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_cryptocurrencies"
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text, "html")

table = soup.find_all('table')[1]

world_title = table.find_all('th')

world_table_title = [title.text.strip() for title in world_title]

df = pd.DataFrame(columns = world_table_title )
df

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)

    length = len(df)
    df.loc[length] = individual_row_data

#['2009', 'Bitcoin', 'BTC,[3] XBT, ₿', 'Satoshi Nakamoto', 'SHA-256d[4][5]', 'C++[6]', 'PoW[5][7]', 'The first and most widely used decentralized ledger currency,[8] with the highest market capitalization as of 2018[update].[9]']
['2011', 'Litecoin', 'LTC, Ł', 'Charlie Lee', 'Scrypt', 'C++[10]', 'PoW', 'One of the first cryptocurrencies to use scrypt as a hashing algorithm.']
['2011', 'Namecoin', 'NMC', 'Vincent Durham[11][12]', 'SHA-256d', 'C++[13]', 'PoW', 'Also acts as an alternative, decentralized DNS.']
['2012', 'Peercoin', 'PPC', 'Sunny King(pseudonym)[citation needed]', 'SHA-256d[citation needed]', 'C++[14]', 'PoW & PoS', 'The first cryptocurrency to use both PoW and PoS functions.']
['2013', 'Dogecoin', 'DOGE, XDG, Ð', 'Jackson Palmer& Billy Markus[15]', 'Scrypt[16]', 'C++[14]', 'PoW', 'Based on the Doge internet meme.']
['2013[17][18]', 'Gridcoin', 'GRC', 'Rob Hälford[19]', 'Scrypt', 'C++[20]', 'Decentralized PoS', 'Linked to citizen science through the Berkeley Open Infrastructure for Network Computing[21]']
['2013', 'Primecoin', 'XPM', 'Sunny King(pseudonym)[22][23]', '1CC/2CC/TWN[24]', 'TypeScript, C++[25]', 'PoW[24]', 'Uses the finding of prime chains composed of Cunningham chains and bi-twin chains for proof-of-work.']
['2013', 'Ripple[26][27]', 'XRP', 'Chris Larsen &Jed McCaleb[28]', 'ECDSA[29]', 'C++[30]', '"Consensus"', 'Designed for peer-to-peer debt transfer. Not based on bitcoin.']
['2013', 'Nxt', 'NXT', 'BCNext(pseudonym)', 'SHA-256d[31]', 'Java[32]', 'PoS', 'Specifically designed as a flexible platform to build applications and financial services around its protocol.']
['2014', 'Auroracoin', 'AUR', 'Baldur Odinsson(pseudonym)[33]', 'Scrypt', 'C++[34]', 'PoW', 'Created as an alternative currency for Iceland, intended to replace the Icelandic króna.']
['2014', 'Dash', 'DASH', 'Evan Duffield[35][36]', 'X11', 'C++[37]', 'PoW & Proof of Service[nt 1]', 'A bitcoin-based currency featuring instant transactions, decentralized governance and budgeting, and private transactions.']
['2014', 'NEO', 'NEO', 'Da Hongfei & Erik Zhang', 'SHA-256 & RIPEMD160', 'C#[38]', 'dBFT', 'China based cryptocurrency, formerly ANT Shares and ANT Coins. The names were changed in 2017 to NEO and GAS.']
['2014', 'MazaCoin', 'MZC', 'BTC Oyate Initiative', 'SHA-256d', 'C++[39]', 'PoW', 'The underlying software is derived from that of another cryptocurrency, ZetaCoin.']
['2014', 'Monero', 'XMR', 'Monero Core Team', 'RandomX', 'C++[40]', 'PoW', 'Privacy-centric coin based on the CryptoNote protocol with improvements for scalability and decentralization.']
['2014', 'Titcoin', 'TIT', 'Edward Mansfield & Richard Allen[41]', 'SHA-256d', 'TypeScript, C++[42]', 'PoW', 'The first cryptocurrency to be nominated for a major adult industry award.[43]']
['2014', 'Verge', 'XVG', 'Sunerok', 'Scrypt, x17, groestl, blake2s, and lyra2rev2', 'C, C++[44]', 'PoW', 'Features anonymous transactions using Tor.']
['2014', 'Stellar', 'XLM', 'Jed McCaleb', 'Stellar Consensus Protocol (SCP) [45]', 'C, C++[46]', 'Stellar Consensus Protocol (SCP) [45]', 'Open-source, decentralized global financial network.']
['2014', 'Vertcoin', 'VTC', 'David Muller[47]', 'Verthash[48]', 'C++[49]', 'PoW', 'Aims to be ASIC resistant.']
['2015', 'Ethereum', 'ETH, Ξ', 'Vitalik Buterin[50]', 'Ethash[51]', 'C++, Go[52]', 'PoW, PoS', 'Supports Turing-complete smart contracts.']
['2015', 'Ethereum Classic', 'ETC', '', 'EtcHash/Thanos[53]', '', 'PoW', 'An alternative version of Ethereum[54] whose blockchain does not include the DAO hard fork.[55] Supports Turing-complete smart contracts.']
['2015', 'Nano', 'XNO, Ӿ', 'Colin LeMahieu', 'Blake2', 'C++[citation needed]', 'Open Representative Voting[56]', 'Decentralized, feeless, open-source, peer-to-peer cryptocurrency. First to use a Block Lattice structure.']
['2015', 'Tether', 'USDT', 'Jan Ludovicus van der Velde[57]', 'Omnicore[58]', '', 'PoW', 'Tether claims to be backed by USD at a 1 to 1 ratio. The company has been unable to produce promised audits.[59]']
['2016', 'Firo', 'FIRO', 'Poramin Insom[60]', 'Merkle tree Proof[61]', 'C++[62]', 'PoW', "The first financial system employing Zero-knowledge proof to protect users' privacy.[60] It conducted the world's first large-scale blockchain election for Thailand Democrat Party in 2018.[63]"]
['2016', 'Zcash', 'ZEC', 'Zooko Wilcox', 'Equihash', 'C++[64]', 'PoW', 'The first open, permissionless financial system employing zero-knowledge security.']
['2017', 'Bitcoin Cash', 'BCH[65]', '', 'SHA-256d', '', 'PoW', 'Hard fork from bitcoin, increased maximum block size from 1MB to 8MB (as of 2018[update], 32MB)']
['2017', 'EOS.IO', 'EOS', 'Dan Larimer', '', 'WebAssembly, Rust, C, C++[66]', 'delegated PoS', 'Feeless Smart contract platform for decentralized applications and decentralized autonomous corporations with a block time of 500 ms.[66]']
['2017', 'Cardano', 'ADA, ₳', 'Charles Hoskinson', 'Ouroboros, PoS Algorithm[67]', 'Haskell[68]', 'PoS', 'Proof-of-stake blockchain platform: developed via evidence-based methods and peer-reviewed research.[69][70][71]']
['2017', 'Tron', 'TRX', 'Justin Sun', '', 'Java, Solidity[72]', '', '']
['2018', 'AmbaCoin', '', '', '', '', '', 'official cryptocurrency of the Cameroonian separatist entity of Ambazonia']
['2018', 'Nervos Network', 'CKB', 'Kevin Wang, Daniel Lv, Terry Tai', 'Eaglesong', 'Rust, JavaScript, C', 'PoW', 'Multi-layered blockchain smart contract platform[73]']
['2019', 'Algorand', 'ALGO', 'Silvio Micali', '', 'Go[74]', 'PoS', 'Uses a verifiable random function to randomly select groups of users to certify blocks.[75]']
['2020', 'Avalanche', 'AVAX', 'Emin Gün Sirer, Kevin Sekniqi, Maofan "Ted" Yin', '', '', 'PoS', '']
['2020', 'Shiba Inu', 'SHIB', 'Ryoshi', '', '', 'PoS', '']
['2020', 'Polkadot', 'DOT', 'Gavin Wood', '', 'Rust', 'PoS', '']
['2020', 'Solana', 'SOL', 'Anatoly Yakovenko', '', 'Rust', 'PoS', '']
['2021', 'DeSo', 'DESO', 'Nader al-Naji (aka diamondhands)[76]', '', 'Go[77]', 'PoW[78]', 'Also a social media platform, resembling Twitter.[79][80] Known as BitClout until September 2021.[76]']
['2021', 'SafeMoon', 'SAFEMOON', 'SafeMoon LLC', '', 'Solidity[81]', 'PoW', '']
['2023', 'Arkham Intel Exchange', 'ARKM[82][83]', 'Miguel Morel', '', 'Solidity', 'PoS', '']

df.to_csv(r'C:\Users\ANURAG\Downloads\token.csv', index = False)
