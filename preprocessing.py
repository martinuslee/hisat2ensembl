import os
from Bio import SeqIO
import random

species = "Gopherus_agassizii"
sample = "SRR7610696_1.fastq"
sample2 = "SRR7610696_2.fastq"

record_dict, record2_dict= SeqIO.index(f"3.SAMPLE/{species}/{sample}", "fastq"), SeqIO.index(f"3.SAMPLE/{species}/{sample2}", "fastq")

sampleRecords, sampleRecords_2 = [], []

print('read ok')
keys = random.sample(list(record_dict), 10)
keys = sorted(keys)

print('key ok')
print(keys)

for k in keys:
    sampleRecords.append(record_dict[k])
    sampleRecords_2.append(record2_dict[k])

for i in range(len(sampleRecords)):
    SeqIO.write(sampleRecords, f"3.SAMPLE/{species}/r10_{sample}", "fastq")
    SeqIO.write(sampleRecords_2, f"3.SAMPLE/{species}/r10_{sample2}", "fastq")